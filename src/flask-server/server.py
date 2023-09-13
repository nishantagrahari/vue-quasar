from flask import Flask,jsonify,request
from flask import make_response 
import psycopg2 
from flask_cors import CORS
from flask_cors import cross_origin
import json

app=Flask(__name__)
CORS(app,supports_credentials=True)
CORS(app, origins="http://localhost:8080")
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(__name__)


# Crediantials
hostname ='oata.cugydhczfi8r.us-west-2.rds.amazonaws.com'
database='oata'
username='postgres_admin'
pwd='oata_aff123'
port_id=5432

#connection & cursor initialization
conn= None  
cur= None

#Local host credentials
conn= psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
)


# CORS(app,resources={r""})

@app.route('/master-filter/<s>',methods=['GET','POST'])
def getstate(s):
    cur=conn.cursor()
    
    
    if(request.method=='POST'):
        newState=""
        post_data=request.get_json()    
        print("territary date",post_data)
        newState=str(post_data.get('state'))[1:-1]
        print('new terrritory data',newState)

    
    if( s == 'state'):
         create_script = '''select distinct(org_state_name) from test.test_table7 tt order by org_state_name asc''' 
    else:
         create_script = f'''select distinct (org_territory) from test.org_state_territory ost where org_state_name in ({newState}) order by org_territory asc '''            
   
    
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})

@app.route('/',methods=['GET'])
def home():   
        cur=conn.cursor() 
        create_script = ''' select "ORG_TIER",count(distinct("ORG_ID"))as HCP,count(distinct("ACC_ID")) as ACCOUNT,count(distinct("IND_NPI")) as PHYSICIAN,sum("ORG_PRODUCT_SALES")/10000 as SALES
                            from test."Test_Table5"
                            group by "ORG_TIER"
                            order by case 
                            WHEN "ORG_TIER" = 'H' then 1
                            WHEN "ORG_TIER" = 'M' then 2 
                            WHEN "ORG_TIER" = 'L' then 3
                            END ASC ''' 
        
        cur.execute(create_script)
        res=cur.fetchall()
        # print((name))
        return ({"output":res})

    # except Exception as error:
    #     return (error)
    # finally:
    #     if cur is not None:
    #         cur.close()
    #     if conn is not None:
    #         conn.close()

@app.route('/Medium/<s>',methods=['GET'])
def Tier(s):
    # return (s)  
    cur=conn.cursor() 
    create_script = f""" select CONCAT('D',a.DECILE),a.ORG,a.ACCOUNT,a.PHYSICIAN,a.SALES,a.POT from 
                        (	
                            select "org_decile" AS DECILE,count(distinct("org_id"))as ORG,count(distinct("acc_id")) as ACCOUNT,count(distinct("ind_npi")) as PHYSICIAN,sum("org_product_sales")/10000 as SALES,'29%' as POT
                            from test."test_table7"
                            where "org_tier"='{s}'
                            group by "org_decile"
                            order by "org_decile" desc
                        )a """
                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})


@app.route('/Chart/<s>',methods=['GET','POST'])
def Chartt(s):
    # return (s)
    newState=""
    newTerr=""
    checkStateSelected= True 
    cur=conn.cursor()

    post_data=request.get_json()    
    print(post_data)
    newState=str(post_data.get('state'))[1:-1]
    newTerr=str(post_data.get('terr'))[1:-1]
    checkStateSelected=bool(post_data.get('isstateselected'))

    print('new data chart1',newState,newTerr,checkStateSelected)
    print('checkStateSelected chart2',checkStateSelected)

   

    if(s =='Potential'):
                if(newState!=""):           
                        if(newTerr!="" and checkStateSelected == False):
                            #new territory is selcted and also the state is selected
                            create_script =f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7" where "org_state_name"in ({newState}) and "org_territory" in ({newTerr})) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                                    from test."test_table7" where "org_state_name" in ({newState}) and "org_territory" in ({newTerr})
                                                )a
                                                group by a."org_academic_vs_community"
                                            )b"""

                        else:
                            create_script =f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7" where "org_state_name" in ({newState})) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                                    from test."test_table7" where "org_state_name" in ({newState})
                                                )a
                                                group by a."org_academic_vs_community"
                                            )b"""

                else:
                    create_script ="""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                        from
                                        (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                            (select count(distinct ( "org_id")) from test."test_table7") as total
                                            from
                                            ( 
                                                select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                                from test."test_table7"
                                            )a
                                            group by a."org_academic_vs_community"
                                        )b"""
    else:
                # checking for metrix other than potential
                if(newState!=""):           
                        if(newTerr!="" and checkStateSelected == False):
                            #new territory is selected and also the state is selected
                            create_script =f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7" where "org_ddd_sales">1000 and "org_state_name"in ({newState}) and "org_territory" in ({newTerr})) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                                    from test."test_table7" where "org_ddd_sales">1000 and "org_state_name" in ({newState}) and "org_territory" in ({newTerr})
                                                )a
                                                group by a."org_academic_vs_community"
                                            )b"""

                        else:
                            create_script =f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7" where "org_ddd_sales">1000 and "org_state_name" in ({newState})) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                                    from test."test_table7" where "org_state_name" in ({newState}) and "org_ddd_sales">1000
                                                )a
                                                group by a."org_academic_vs_community"
                                            )b"""

                else:
                    create_script ="""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                        from
                                        (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                            (select count(distinct ( "org_id")) from test."test_table7" where "org_ddd_sales">1000) as total
                                            from
                                            ( 
                                                select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                                from test."test_table7"  where "org_ddd_sales">1000
                                            )a
                                            group by a."org_academic_vs_community"
                                        )b"""


                        
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})





@app.route('/Chart2/<s>',methods=['GET','POST'])
def Chart2(s):
    # return (s)  
    cur=conn.cursor()

    newState=""
    newTerr=""
    checkStateSelected= True 
    cur=conn.cursor()

    post_data=request.get_json()    
    # print(post_data)
    newState=str(post_data.get('state'))[1:-1]
    newTerr=str(post_data.get('terr'))[1:-1]
    checkStateSelected=bool(post_data.get('isstateselected'))

    # print('new data chart2',newState,newTerr,checkStateSelected)
    # print('checkStateSelected chart2',checkStateSelected)

    if(s =='Potential'):
        if(newState!=""):           
                        if(newTerr!="" and checkStateSelected == False):
                            #new territory is selcted and also the state is selected
                            create_script = f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7"  where "org_state_name" in ({newState}) and "org_territory" in ({newTerr})) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                                    from test."test_table7"  where "org_state_name" in ({newState}) and "org_territory" in ({newTerr})
                                                )a
                                                group by a."org_flag_for_340b"
                                            )b """

                        else:
                             create_script = f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7"  where "org_state_name" in ({newState})) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                                    from test."test_table7"  where "org_state_name" in ({newState})
                                                )a
                                                group by a."org_flag_for_340b"
                                            )b """

        else:
                        create_script = """select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7" ) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                                    from test."test_table7" 
                                                )a
                                                group by a."org_flag_for_340b"
                                            )b """
    else:
        if(newState!=""):           
                        if(newTerr!="" and checkStateSelected == False):
                            #new territory is selcted and also the state is selected
                            create_script = f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7"  where "org_state_name" in ({newState}) and "org_territory" in ({newTerr}) and "org_product_sales">100) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                                    from test."test_table7"  where "org_state_name" in ({newState}) and "org_territory" in ({newTerr}) and "org_product_sales">100
                                                )a
                                                group by a."org_flag_for_340b"
                                            )b """

                        else:
                             create_script = f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7"  where "org_state_name" in ({newState})  and "org_product_sales">100) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                                    from test."test_table7"  where "org_state_name" in ({newState})  and "org_product_sales">100
                                                )a
                                                group by a."org_flag_for_340b"
                                            )b """

        else:
                        create_script = """select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                            from
                                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                                (select count(distinct ( "org_id")) from test."test_table7" where "org_product_sales">100 ) as total
                                                from
                                                ( 
                                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                                    from test."test_table7" where "org_product_sales">100
                                                )a
                                                group by a."org_flag_for_340b"
                                            )b """



                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})    




if __name__ == '__main__':
    app.run(debug=True)   

