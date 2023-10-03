import json, unittest, requests, os
from task import create_chart

def return_query(top: int = 2, category: str = "total_enrollment"):
    q = [{"id":1,"category":"All Students","total_enrollment":"162","grade_1":"33","grade_3":"23","grade_5":"18","grade_7":"No Data","female":"79","female_percent":"0.4876543209876543","male_percent":"0.5123456790123457","year":"2015-16","school_name":"P.S. 015 Roberto Clemente","grade_k":"32","grade_2":"39","grade_4":"17","grade_6":"No Data","grade_8":"No Data","male":"83"},{"id":7,"category":"All Students","total_enrollment":"249","grade_1":"43","grade_3":"43","grade_5":"40","grade_7":"No Data","female":"115","female_percent":"0.46184738955823296","male_percent":"0.5381526104417671","year":"2015-16","school_name":"P.S. 019 Asher Levy","grade_k":"47","grade_2":"41","grade_4":"35","grade_6":"No Data","grade_8":"No Data","male":"134"},{"id":13,"category":"All Students","total_enrollment":"535","grade_1":"90","grade_3":"92","grade_5":"92","grade_7":"No Data","female":"252","female_percent":"0.47102803738317756","male_percent":"0.5289719626168224","year":"2015-16","school_name":"P.S. 020 Anna Silver","grade_k":"82","grade_2":"98","grade_4":"81","grade_6":"No Data","grade_8":"No Data","male":"283"}]
    link = create_chart(limit=top, category=category)
    return {"table": q[0:top], "link":link}

class TestCJsonImport(unittest.TestCase):
    def test_importpositive(self):
        data = return_query()
        self.assertTrue(os.path.isfile(data["link"]), "file does not exist")

if __name__ == '__main__':
    unittest.main()


