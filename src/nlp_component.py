class BottleReporter:
    def get_report(self, label, conf):
        status = "DEFECTIVE" if label == 1 else "GOOD"
        return f"Industrial Report: Bottle state is {status} (Confidence: {conf:.2f})."

if __name__ == "__main__":
    print(BottleReporter().get_report(1, 0.95))