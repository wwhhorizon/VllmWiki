# vllm-project/vllm#1525: Output response is truncated

| 字段 | 值 |
| --- | --- |
| Issue | [#1525](https://github.com/vllm-project/vllm/issues/1525) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Output response is truncated

### Issue 正文摘录

I am using the below LLM code in MLserver which uses vLLM framework ``` class MyCustomRuntime(MLModel): """ Model template. You can load your model parameters in __init__ from a location accessible at runtime """ async def load(self) -> bool: """ Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest. """ print("Initializing.................") login(token=access_token) self.llm = LLM(model=model_name) return True @decode_args async def predict(self, chat: np.ndarray) -> np.ndarray: y = self.llm.generate(chat[0]) print("answer ", y) return np.asarray([y]) ``` When i run the inference via ML server, it gives me truncated results ``` samuel@samuel-dev-vm001:~/repos/dbg$ python inference-llm.py Elapsed time: 0.40654778480529785 { "model_name": "70b", "id": "ecebfd7d-4930-4b32-a2e8-b78a41edf7bc", "parameters": {}, "outputs": [ { "name": "output-0", "shape": [ 1, 1 ], "datatype": "BYTES", "parameters": { "content_type": "np" }, "data": [ { "request_id": "0", "prompt": "How can i be a better person", "prompt_token_ids": [ 1, 1128, 508, 474, 367, 263, 2253, 2022 ], "outputs": [ {...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: code in MLserver which uses vLLM framework ``` class MyCustomRuntime(MLModel): """ Model template. You can load your model parameters in __init__ from a location accessible at runtime """ async def load(self) -> bool: "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oken) self.llm = LLM(model=model_name) return True @decode_args async def predict(self, chat: np.ndarray) -> np.ndarray: y = self.llm.generate(chat[0]) print("answer ", y) return np.asarray([y]) ``` When i run the infer...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Output response is truncated I am using the below LLM code in MLserver which uses vLLM framework ``` class MyCustomRuntime(MLModel): """ Model template. You can load your model parameters in __init__ from a location acc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
