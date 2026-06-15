# vllm-project/vllm#3296: v0.3.3 vllm.entrypoints.openai.api_server  error

| 字段 | 值 |
| --- | --- |
| Issue | [#3296](https://github.com/vllm-project/vllm/issues/3296) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> v0.3.3 vllm.entrypoints.openai.api_server  error

### Issue 正文摘录

1. GPU：4090 * 4 2. `pip install vllm==0.3.3` 3. `python3 -m vllm.entrypoints.openai.api_server --model /Llama-2-7B-Chat-hf/ --engine-use-ray --host 0.0.0.0 --port 8080 --worker-use-ray --max-num-seqs 64 --tensor-parallel-size 4` 4. When I send a request：![image](https://github.com/vllm-project/vllm/assets/42427430/92e6ca0f-8f49-4800-b8d7-fc4981c57323) 5. The following error occurs![image](https://github.com/vllm-project/vllm/assets/42427430/4354f758-e1ce-4345-a3a0-4ea1b29c5108)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stall vllm==0.3.3` 3. `python3 -m vllm.entrypoints.openai.api_server --model /Llama-2-7B-Chat-hf/ --engine-use-ray --host 0.0.0.0 --port 8080 --worker-use-ray --max-num-seqs 64 --tensor-parallel-size 4` 4. When I send a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: v0.3.3 vllm.entrypoints.openai.api_server error 1. GPU：4090 * 4 2. `pip install vllm==0.3.3` 3. `python3 -m vllm.entrypoints.openai.api_server --model /Llama-2-7B-Chat-hf/ --engine-use-ray --host 0.0.0.0 --port 8080 --w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: use-ray --max-num-seqs 64 --tensor-parallel-size 4` 4. When I send a request：![image](https://github.com/vllm-project/vllm/assets/42427430/92e6ca0f-8f49-4800-b8d7-fc4981c57323) 5. The following error occurs![image](http...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
