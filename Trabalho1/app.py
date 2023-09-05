from flask import Flask, render_template, request
import statistics

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        data = request.form.get("data")
        data = [float(x.strip()) for x in data.split(",")]

        mean = statistics.mean(data)
        median = statistics.median(data)
        mode = statistics.mode(data)
        variance = statistics.variance(data)
        std_dev = statistics.stdev(data)

        return render_template("result.html", mean=mean, median=median, mode=mode, variance=variance, std_dev=std_dev)
    
    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)
