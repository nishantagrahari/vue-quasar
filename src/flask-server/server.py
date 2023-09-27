from flask import Flask, jsonify, request
from flask import make_response
import psycopg2
from flask_cors import CORS
from flask_cors import cross_origin
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(__name__)


# Crediantials
hostname = 'oata.cugydhczfi8r.us-west-2.rds.amazonaws.com'
database = 'oata'
username = 'postgres_admin'
pwd = 'oata_aff123'
port_id = 5432

# connection & cursor initialization
conn = None
cur = None

# Local host credentials
conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id
)


def check_state_territory(newState):
    # checking for state and terriroty filter and updating params based on it
    orgStateName = ""
    # orgTerritoryName = ""

    if (newState == ""):
        orgStateName = True
        # orgTerritoryName = True
    else:       
        orgStateName = f"org_state_name in ({newState})"       

    return (orgStateName)

def check_tier(newTier):
    orgTierName= ""

    if(newTier == 'H' or newTier== 'M' or newTier=='L'):
        orgTierName = f"org_tier = '{newTier}'"
    elif(newTier == 'null'):
        orgTierName = 'org_tier is NULL'
    elif('D' in newTier):
        temp = newTier.split('D')
        orgTierName= f"org_decile = {temp[1]}"
    else:
        orgTierName=True
    
    return orgTierName



@app.route('/map', methods=['GET', 'POST'])
def map():
    cur = conn.cursor()
    newState = ""   
    newTier= ""   
    post_data = request.get_json()


    # Removing [] from the items

    newState = str(post_data.get('state'))[1:-1]
    # newTerr = str(post_data.get('terr'))[1:-1]
    # checkStateSelected = bool(post_data.get('isstateselected'))
    newTier=str(post_data.get('tier'))

    # print('new data map', newState, newTerr, checkStateSelected)

    # Changing param best on the state and Territory filter

    orgStateName= check_state_territory(newState)
    orgTierName=check_tier(newTier)
    
    print('new map data', orgStateName,orgTierName)



    create_script = f"""select org_geo_coord_x ,org_geo_coord_y, org_market_sales_ind13
                        from test.test_table9
                        where {orgStateName} and {orgTierName}                       
                        order by org_market_sales_ind13 desc"""

    cur.execute(create_script)
    res = cur.fetchall()   
    print("here is map data")
    # print(res)
    # print((name))

    return ({"output": res})


@app.route('/states', methods=['GET'])
def get_data_states():

    try:

        cursor = conn.cursor()

        # Assuming 'public.map' is your table name
        query = "SELECT DISTINCT org_state FROM test.test_table7"

        cursor.execute(query)
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        result = []
        for row in data:
            result.append(dict(zip(column_names, row)))
        cursor.close()
        return jsonify(result)  # Return the result as JSON
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of an exception
        return jsonify({'error': str(e)})


@app.route('/master-filter/<s>', methods=['GET', 'POST'])
def getstate(s):
    cur = conn.cursor()

    if (request.method == 'POST'):
        newState = ""
        post_data = request.get_json()
        print("territary date", post_data)
        newState = str(post_data.get('state'))[1:-1]
        print('new terrritory data', newState)

    if (s == 'state'):
        create_script = '''select distinct(org_state_name) from test.test_table7 tt order by org_state_name asc'''
    else:
        create_script = f'''select distinct (org_territory) from test.org_state_territory ost where org_state_name in ({newState}) order by org_territory asc '''

    cur.execute(create_script)
    res = cur.fetchall()
    # print((name))
    return ({"output": res})


@app.route('/table/tier',methods=['GET','POST'])
def home():   
        cur=conn.cursor()
        newState=""
        # newTerr=""
        # checkStateSelected= True       

        post_data=request.get_json()    
        # print(post_data)

        #Removing [] from the items
        newState=str(post_data.get('state'))[1:-1]
        # newTerr=str(post_data.get('terr'))[1:-1]
        checkStateSelected=bool(post_data.get('isstateselected'))

        print('new data Tier',newState)
        # print('checkStateSelected Tier',checkStateSelected)

        orgStateName=check_state_territory(newState)

        create_script=f'''select coalesce("org_tier",'Total') as org_tier,
                        cast (sum("org") as INT) as "org",cast(sum("account") as INT) as account,cast(sum(physician) as INT) as physician,cast(sum(product_sales) as INT) as product_sales,cast(sum(Potential) as INT) as Potential,cast(sum(Product_A_sales) as INT) as product_a_sales,cast(sum(Product_B_sales) as INT) as product_b_sales,cast(sum(Diagnosed_Pats) as INT) as diagnosed_pats,cast(sum(Treated_pats) as INT) as treated_pats
                        from
                        (	
                            select t2.*,coalesce(t1.ORG,0) as org,coalesce(t1.ACCOUNT,0) as account,coalesce(t1.PHYSICIAN,0) as physician,coalesce(t1.PRODUCT_SALES,0) as product_sales,coalesce(t1.Potential,0) as Potential,
                            coalesce (t1.Product_A_sales,0) as Product_A_sales,coalesce(t1.Product_B_sales,0)as Product_B_sales,coalesce (t1.Diagnosed_Pats,0) as Diagnosed_Pats,coalesce (t1.Treated_Pats,0) as Treated_Pats
                            from 
                            (
                                select coalesce("org_tier",'NT') as org_tier,count(distinct("org_id"))as ORG,sum("org_number_of_accounts") as ACCOUNT,sum("org_number_of_hcps") as PHYSICIAN,sum("org_product_sales") as PRODUCT_SALES,
                                Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where {orgStateName}) as decimal),0) as Potential,
                                Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where {orgStateName}) as decimal),0) as Product_A_sales,
                                Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where {orgStateName}) as decimal),0) as Product_B_sales,
                                Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where {orgStateName}) as decimal),0) as Diagnosed_Pats,
                                Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where {orgStateName}) as decimal),0) as Treated_Pats
                                from test.test_table9
                                where {orgStateName}
                                group by "org_tier"	
                            )t1 
                            right join 
                            (select distinct coalesce("org_tier",'NT') as "org_tier" 
                            from test.test_table9)t2
                            on t1.org_tier=t2.org_tier                            
                        )a 
                        group by rollup ("org_tier")
                        order by case 
                        WHEN a."org_tier" = 'H' then 1
                        WHEN a."org_tier" = 'M' then 2 
                        WHEN a."org_tier" = 'L' then 3
                        WHEN a."org_tier" = 'NT' then 4
                        WHEN a."org_tier" = 'Total' then 5
                        END asc'''
        
        cur.execute(create_script)
        res=cur.fetchall()
        return ({"output":res})


@app.route('/table/decile/<s>',methods=['GET','POST'])
def Tier(s):     
    cur=conn.cursor()
    newState=""
    # newTerr=""
    # checkStateSelected= True     
    post_data=request.get_json()

    # print(post_data)
    #Removing [] from the items
    newState=str(post_data.get('state'))[1:-1]
    # newTerr=str(post_data.get('terr'))[1:-1]
    # checkStateSelected=bool(post_data.get('isstateselected'))

    print('new data chart1',newState)    
     #Changing param best on the state and Territory filter 
    orgStateName=check_state_territory(newState)    

    create_script = f""" select CONCAT('D',a.decile) as Decile,a.org,a.account,a.physician,a.product_sales,a.Potential,a.Product_A_sales,a.Product_B_sales,a.Diagnosed_Pats,a.Treated_Pats from 
                        (	
                            select "org_decile" AS decile,count(distinct("org_id"))as org,sum("org_number_of_accounts") as account,sum("org_number_of_hcps") as physician,
                            sum("org_product_sales") as product_sales,
                            concat(Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where "org_tier"='{s}' and {orgStateName}) as decimal),0),'%') as Potential,
                            concat(Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where "org_tier"='{s}'and {orgStateName}) as decimal),0),'%') as Product_A_sales,
                            concat(Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where "org_tier"='{s}' and {orgStateName}) as decimal),0),'%') as Product_B_sales,
                            concat(Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where "org_tier"='{s}' and {orgStateName}) as decimal),0),'%') as Diagnosed_Pats,
                            concat(Round(sum("org_market_sales_ind13")*100/cast((select sum("org_market_sales_ind13") from test.test_table9 where "org_tier"='{s}' and {orgStateName}) as decimal),0),'%') as Treated_Pats
                            from test."test_table9"
                            where "org_tier"='{s}' and {orgStateName}
                            group by "org_decile"
                            order by "org_decile" desc
                        )a"""
                
    cur.execute(create_script)
    res=cur.fetchall()
    
    print("look at data")
    # print(res)
    return ({"output":res})


@app.route('/Chart1/<s>',methods=['GET','POST'])
def Chartt(s):
    # return (s)
    newState=""
    # newTerr=""
    # checkStateSelected= True 
    newTier=""
    cur=conn.cursor()

    post_data=request.get_json()    
    # print(post_data)
    newState=str(post_data.get('state'))[1:-1]
    # newTerr=str(post_data.get('terr'))[1:-1]
    # checkStateSelected=bool(post_data.get('isstateselected'))
    newTier=str(post_data.get('tier'))

   
    # print('chart1',newState,newTerr,checkStateSelected,newTier)    
     #Changing param best on the state and Territory filter 
    orgStateName=check_state_territory(newState)
    orgTierName=check_tier(newTier)

    print("new chart Tier name",orgTierName)  

    if(s =='Potential'):
        create_script =f"""select d.*,coalesce(c.countt,0) as accounts,coalesce(c.total,0) as total_accounts,coalesce(c.per,0) as per
                            from
                            (
                                select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                from
                                (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                    (select count(distinct ( "org_id")) from test."test_table9" where {orgStateName} and {orgTierName}) as total
                                    from
                                    ( 
                                        select "org_id" as org,"org_academic_vs_community","org_market_sales_ind13"
                                        from test."test_table9" where {orgStateName} and {orgTierName}
                                    )a
                                    group by a."org_academic_vs_community"
                                )b
                            )c
                            right join 
                            (select distinct ("org_academic_vs_community") from test."test_table9")d
                            on c."org_academic_vs_community"=d."org_academic_vs_community"
                            order by d."org_academic_vs_community" asc"""                   
    else:
                # checking for metrix other than potential
                create_script =f"""select d.*,coalesce(c.countt,0) as accounts,coalesce(c.total,0) as total_accounts,coalesce(c.per,0) as per
                                    from
                                    (
                                        select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                        from
                                        (	select a."org_academic_vs_community",count(distinct(a.org)) as countt,
                                            (select count(distinct ( "org_id")) from test."test_table9" where {orgStateName} and {orgTierName} and "org_market_sales_ind13">100) as total
                                            from
                                            ( 
                                                select "org_id" as org,"org_academic_vs_community","org_market_sales_ind13"
                                                from test."test_table9" where {orgStateName} and {orgTierName} and "org_market_sales_ind13">100
                                            )a
                                            group by a."org_academic_vs_community"
                                        )b
                                    )c
                                    right join 
                                    (select distinct ("org_academic_vs_community") from test."test_table9")d
                                    on c."org_academic_vs_community"=d."org_academic_vs_community"
                                    order by d."org_academic_vs_community" asc"""
                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})


@app.route('/Chart2/<s>',methods=['GET','POST'])
def Chart2(s):
    # return (s)  
    cur=conn.cursor()

    newState=""
    # newTerr=""
    newTier=""
    # checkStateSelected= True 
    cur=conn.cursor()

    post_data=request.get_json()    
    # print(post_data)
    newState=str(post_data.get('state'))[1:-1]
    # newTerr=str(post_data.get('terr'))[1:-1]
    # checkStateSelected=bool(post_data.get('isstateselected'))
    newTier=str(post_data.get('tier'))

    orgStateName=check_state_territory(newState)
    orgTierName=check_tier(newTier)

    print("new chart2 Tier name",orgTierName)   

    if(s =='Potential'):
         create_script=f"""select d.*,coalesce(c.countt,0) as accounts,coalesce(c.total,0) as total_accounts,coalesce(c.per,0) as per
                            from
                            (
                                select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                from
                                (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                    (select count(distinct ( "org_id")) from test."test_table9"  where {orgStateName} and {orgTierName}) as total
                                    from
                                    ( 
                                        select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                        from test."test_table9"  where {orgStateName} and {orgTierName}
                                    )a
                                    group by a."org_flag_for_340b"
                                )b
                            )c
                            right join 
                            (select distinct "org_flag_for_340b" from test."test_table9")d
                            on c."org_flag_for_340b"= d."org_flag_for_340b"
                            order by d."org_flag_for_340b" asc """  
                        
    else:
        create_script=f"""select d.*,coalesce(c.countt,0) as accounts,coalesce(c.total,0) as total_accounts,coalesce(c.per,0) as per
                            from
                            (
                                select b.*,cast((cast(b.countt as decimal)/cast(b.total as decimal))*100 as integer) as per
                                from
                                (	select a."org_flag_for_340b",count(distinct(a.org)) as countt,
                                    (select count(distinct ( "org_id")) from test."test_table9"  where {orgStateName} and {orgTierName} and "org_market_sales_ind13">100) as total
                                    from
                                    ( 
                                        select  "org_id" as org,"org_flag_for_340b","org_product_sales"
                                        from test."test_table9"  where {orgStateName} and {orgTierName} and "org_market_sales_ind13">100
                                    )a
                                    group by a."org_flag_for_340b"
                                )b
                            )c
                            right join 
                            (select distinct "org_flag_for_340b" from test."test_table9")d
                            on c."org_flag_for_340b"= d."org_flag_for_340b"
                            order by d."org_flag_for_340b" asc """  
        
                
    cur.execute(create_script)
    res=cur.fetchall()
    # print((name))
    return ({"output":res})


if __name__ == '__main__':
    app.run(debug=True)
