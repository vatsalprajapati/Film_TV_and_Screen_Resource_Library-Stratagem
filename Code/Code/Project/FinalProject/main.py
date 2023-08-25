from flask import Flask , render_template , request ,   redirect , g , current_app , url_for
from flask_sqlalchemy import *
import warnings

warnings.filterwarnings('ignore')

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///MRP_DB.db'

db= SQLAlchemy(app)

class STG_FUNDING(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Project = db.Column(db.String)
    Company = db.Column(db.String)
    Year = db.Column(db.String)
    Content_Type = db.Column(db.String)
    Fund = db.Column(db.String)
    Activity = db.Column(db.String)
    Genre = db.Column(db.String)
    Delivery_Method = db.Column(db.String)
    Region = db.Column(db.String)
    Program = db.Column(db.String)
    Status = db.Column(db.String)
    Load_date = db.Column(db.String)
    Backend_Table = db.Column(db.String)

class STG_FUNDING1(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Recipient_Name = db.Column(db.String)
    Recipient_Type = db.Column(db.String)
    Recipient_City = db.Column(db.String)
    Year = db.Column(db.String)
    Approval_Date = db.Column(db.String)
    Amount = db.Column(db.String)
    Recipient_Province = db.Column(db.String)
    Recipient_Postal_Code = db.Column(db.String)
    Federal_Riding = db.Column(db.String)
    Canada_Council_Arts_Program_Discipline = db.Column(db.String)
    Canada_Council_Arts_Section = db.Column(db.String)

class STG_FUNDING2(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Project = db.Column(db.String)
    Company = db.Column(db.String)
    Fiscal_Year = db.Column(db.String)
    Activity = db.Column(db.String)
    Cost = db.Column(db.String)
    Region = db.Column(db.String)
    Program = db.Column(db.String)
    Language = db.Column(db.String)
    Content_Type = db.Column(db.String)

class STG_LINKS_TO_PDF(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String)
    Description = db.Column(db.String)
    LinkToPdf = db.Column(db.String)
    Load_date = db.Column(db.String)
    Backend_Table = db.Column(db.String)

class STG_UNION(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Union = db.Column(db.String)
    Craft_Name = db.Column(db.String)
    Location = db.Column(db.String)
    Telephone= db.Column(db.String)
    Fax = db.Column(db.String)
    Load_date = db.Column(db.String)
    Backend_Table = db.Column(db.String)

class STG_WORKFORCE(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String)
    Name = db.Column(db.String)
    Location = db.Column(db.String)
    Telephone= db.Column(db.String)
    Email = db.Column(db.String)
    Availability = db.Column(db.String)
    Load_date = db.Column(db.String)
    Backend_Table = db.Column(db.String)


class STG_PRODUCTION_UNITS(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String)
    Min_Project_Size = db.Column(db.String)
    Location = db.Column(db.String)
    Wage= db.Column(db.String)
    Website= db.Column(db.String)
    Team_size = db.Column(db.String)
    Load_date = db.Column(db.String)
    Backend_Table = db.Column(db.String)

class STG_INFRASTRUCTURE(db.Model):


    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Company = db.Column(db.String)
    Comments = db.Column(db.String)
    Location = db.Column(db.String)
    Load_date = db.Column(db.String)
    Backend_Table = db.Column(db.String)



@app.route('/workforce/<int:page_num>')
def page(page_num):
    STGs=STG_FUNDING.query.order_by(STG_FUNDING.Project.desc(),STG_FUNDING.Company.desc()).paginate(per_page=50,page=page_num,error_out=True)
    #STGs = STG_FUNDING.query.order_by(STG_FUNDING.Project.desc()).paginate(per_page=100, page=page_num, error_out=True)
    ##STGs = STG_FUNDING.query.paginate(per_page=100, page=page_num, error_out=True)
    return  render_template('index.html',data=STGs)

@app.route('/pdf/<int:page_num>')
def page2(page_num):
    STG2s=STG_LINKS_TO_PDF.query.paginate(per_page=10,page=page_num,error_out=True)
    return  render_template('index2.html',data=STG2s)

@app.route('/union/<int:page_num>')
def page3(page_num):
    STG3s=STG_UNION.query.paginate(per_page=50,page=page_num,error_out=True)
    return  render_template('index3.html',data=STG3s)

@app.route('/workforce2/<int:page_num>')
def page4(page_num):
    ##STG4s=STG_WORKFORCE.query.paginate(per_page=100,page=page_num,error_out=True)
    STG4s=STG_WORKFORCE.query.order_by(STG_WORKFORCE.Location.desc()).paginate(per_page=50,page=page_num,error_out=True)
    return  render_template('index4.html',data=STG4s)

@app.route('/clutch/<int:page_num>')
def page5(page_num):
    STG5s=STG_PRODUCTION_UNITS.query.paginate(per_page=50,page=page_num,error_out=True)
    return  render_template('index5.html',data=STG5s)

@app.route('/infra/<int:page_num>')
def page6(page_num):
    STG6s=STG_INFRASTRUCTURE.query.paginate(per_page=50,page=page_num,error_out=True)
    return  render_template('index6.html',data=STG6s)


@app.route('/Integration')
def Integrate():
    #STG6s=STG_INFRASTRUCTURE.query
    return  render_template('Integration.html',data=STG_FUNDING.query.limit(10) , data2=STG_LINKS_TO_PDF.query.limit(10) ,
                            data3=STG_UNION.query.limit(10))

#@app.route('/')
#def land():
#    return  render_template('Land.html')

@app.route('/')
def main():
    return  render_template('Main.html')

if __name__ == "__main__":
    app.run(debug=True)