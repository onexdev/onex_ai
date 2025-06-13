from gna import GNAEngine

class GNADetector:
    def __init__(self):
        # muatan model pada GNA hardware
        self.engine = GNAEngine.load_model("quantum_gnn_rugpull")

    def detect(self, features):
        # inference cepat mikrodetik
        graph_tensor = features.to_tensor()
        prob = self.engine.infer(graph_tensor)
        return float(prob * 100)  # skor 0–100
