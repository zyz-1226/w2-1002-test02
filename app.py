from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    topic = ""
    feedback = ""
    student_answer = ""
    question_text = "請先選擇學習主題"
    
    if request.method == "POST":
        topic = request.form.get("topic", "")
        action = request.form.get("action", "")
        print("我選擇的主題:", topic)
        
        if topic == "輸入輸出":
            question_text = "Python 使用哪個函式顯示文字？"
        else:
            question_text = "尚未放置題目"
            
        # 判斷是否按下「提交答案」
        if action == "check" and topic == "輸入輸出":
            student_answer = request.form.get("student_answer", "")
            
            # 檢查答案是否正確
            if student_answer == "B":
                feedback = "答對了！"
            else:
                feedback = "答錯了！"
            
    
    return render_template("index.html", 
                           topic=topic, 
                           question_text=question_text, 
                           feedback=feedback,
                           student_answer=student_answer)

if __name__ == "__main__":
    app.run(debug=True, port=5001)