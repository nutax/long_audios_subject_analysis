from src.layers import *

ResearchLayer(
    StatusLayer(),
    ProgressLayer(),
    ConfigurationLayer(),
    ExperimentLayer(),
    EvaluationLayer(),
    GoldStandardLayer(),
)()
