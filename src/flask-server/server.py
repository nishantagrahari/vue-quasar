from flask import Flask,jsonify
from flask import make_response 
import psycopg2 
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.config.from_object(__name__)


# Crediantials
hostname ='localhost'
database='Test'
username='postgres'
pwd='postgres'
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

@app.route('/',methods=['GET'])
def home():   
        cur=conn.cursor() 
        create_script = ''' select "ORG_TIER",count(distinct("ORG_ID"))as HCP,count(distinct("ACC_ID")) as ACCOUNT,count(distinct("IND_NPI")) as PHYSICIAN,sum("ORG_PRODUCT_SALES")/10000 as SALES
                            from public."Test_Table5"
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
                                select "ORG_DECILE" AS DECILE,count(distinct("ORG_ID"))as ORG,count(distinct("ACC_ID")) as ACCOUNT,count(distinct("IND_NPI")) as PHYSICIAN,sum("ORG_PRODUCT_SALES")/10000 as SALES,'29%' as POT
                                from public."Test_Table5"
                                where "ORG_TIER"='{s}'
                                group by "ORG_DECILE"
                                order by "ORG_DECILE" desc
                            )a """
                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})

@app.route('/Chart/<s>',methods=['GET'])
def Chart(s):
    # return (s)  
    cur=conn.cursor()

    if(s =='Potential'):
        create_script = """select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                            from
                            (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                (select count(distinct ( "org_id")) from public."test_table6" ) as total
                                from
                                ( 
                                    select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                    from public."test_table6"
                                )a
                                group by a."org_academic_vs_community"
                            )b """
    else:
        create_script = f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                            from
                            (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                (select count(distinct ( "org_id")) from public."test_table6" where "org_ddd_sales">1000 ) as total
                                from
                                ( 
                                    select  "org_id" as org,"org_academic_vs_community","org_ddd_sales"
                                    from public."test_table6" where "org_ddd_sales">1000
                                )a
                                group by a."org_academic_vs_community"
                            )b"""
                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})


@app.route('/Chart2/<s>',methods=['GET'])
def Chart2(s):
    # return (s)  
    cur=conn.cursor()

    if(s =='Potential'):
        create_script = """select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                            from
                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                (select count(distinct ( "org_id")) from public."test_table6" ) as total
                                from
                                ( 
                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                    from public."test_table6"
                                )a
                                group by a."org_flag_for_340b"
                            )b """
    else:
        create_script = f"""select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                            from
                            (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                (select count(distinct ( "org_id")) from public."test_table6" where "org_product_sales">100 ) as total
                                from
                                ( 
                                    select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                    from public."test_table6"
                                    where "org_product_sales">100
                                )a
                                group by a."org_flag_for_340b"
                            )b"""
                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})    




if __name__ == '__main__':
    app.run(debug=True)   

