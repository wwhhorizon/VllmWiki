# vllm-project/vllm#13491: [Usage]: How to write scoring script when deploying to a managed Azure machine learning real-time endpoint?

| 字段 | 值 |
| --- | --- |
| Issue | [#13491](https://github.com/vllm-project/vllm/issues/13491) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to write scoring script when deploying to a managed Azure machine learning real-time endpoint?

### Issue 正文摘录

I'd like to deploy my custom model on managed Azure machine learning real-time endpoint. So, I've registered my model, but it's not clear to me how to write a proper scoring script in azure when the model is intended to receive OpenAI API compatible calls. The docs in azure provide this basic sample: ```python import os import logging import json import numpy import joblib def init(): """ This function is called when the container is initialized/started, typically after create/update of the deployment. You can write the logic here to perform init operations like caching the model in memory """ global model # AZUREML_MODEL_DIR is an environment variable created during deployment. # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION) # Please provide your model's folder name if there is one model_path = os.path.join( os.getenv("AZUREML_MODEL_DIR"), "model/sklearn_regression_model.pkl" ) # deserialize the model file back into a sklearn model model = joblib.load(model_path) logging.info("Init complete") def run(raw_data): """ This function is called for every invocation of the endpoint to perform the actual scoring/prediction. In the example we extract the data...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ompatible calls. The docs in azure provide this basic sample: ```python import os import logging import json import numpy import joblib def init(): """ This function is called when the container is initialized/started,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ne learning real-time endpoint? usage;stale I'd like to deploy my custom model on managed Azure machine learning real-time endpoint. So, I've registered my model, but it's not clear to me how to write a proper scoring s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: deploying to a managed Azure machine learning real-time endpoint? usage;stale I'd like to deploy my custom model on managed Azure machine learning real-time endpoint. So, I've registered my model, but it's not clear to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: h = os.path.join( os.getenv("AZUREML_MODEL_DIR"), "model/sklearn_regression_model.pkl" ) # deserialize the model file back into a sklearn model model = joblib.load(model_path) logging.info("Init complete") def run(raw_d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
