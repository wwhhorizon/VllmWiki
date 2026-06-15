# vllm-project/vllm#19588: [Bug]: LLMEngine.add_request can't handle erroneous type of request_id

| 字段 | 值 |
| --- | --- |
| Issue | [#19588](https://github.com/vllm-project/vllm/issues/19588) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLMEngine.add_request can't handle erroneous type of request_id

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When submitting a request with a long request_id, for example, python's uuid4(), I can't get an result by running `engine.step()`, and it seems the program got blocked at engine.step() after several iterations. ```python def test_llm_engine_2(): from vllm import EngineArgs from uuid import uuid4 engine_args = EngineArgs( model="meta-llama/Llama-3.2-1B-Instruct", tensor_parallel_size=1, gpu_memory_utilization=0.8, device="auto", ) example_inputs = [(uuid4(), "What is LLM?", SamplingParams(temperature=0.0))] engine = LLMEngine.from_engine_args(engine_args=engine_args) # Start the engine with an event loop while True: if example_inputs: req_id, prompt, sampling_params = example_inputs.pop(0) engine.add_request(req_id,prompt,sampling_params) print(req_id) # continue the request processing request_outputs = engine.step() for request_output in request_outputs: if request_output.finished: print(request_output) print(f"engine.has_unfinished_requests(): {engine.has_unfinished_requests()}") if not (engine.has_unfinished_requests() or example_inputs): break if __name__ == "__main__": test_llm_engine_2() ``` ![Image](https://github.com/user-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r several iterations. ```python def test_llm_engine_2(): from vllm import EngineArgs from uuid import uuid4 engine_args = EngineArgs( model="meta-llama/Llama-3.2-1B-Instruct", tensor_parallel_size=1, gpu_memory_utilizat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fa) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ineArgs from uuid import uuid4 engine_args = EngineArgs( model="meta-llama/Llama-3.2-1B-Instruct", tensor_parallel_size=1, gpu_memory_utilization=0.8, device="auto", ) example_inputs = [(uuid4(), "What is LLM?", Samplin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: LLMEngine.add_request can't handle erroneous type of request_id bug ### Your current environment ### 🐛 Describe the bug When submitting a request with a long request_id, for example, python's uuid4(), I can't get...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
