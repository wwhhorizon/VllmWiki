# vllm-project/vllm#3898: [Bug]:Failed that we generate the pompts with the google/gemma-2b model by the python code, 

| 字段 | 值 |
| --- | --- |
| Issue | [#3898](https://github.com/vllm-project/vllm/issues/3898) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:Failed that we generate the pompts with the google/gemma-2b model by the python code, 

### Issue 正文摘录

### Your current environment ```text python 3.10.14 vllm 0.4.0.post1 vllm-nccl-cu12 2.18.1.0.1.0 ``` ### the python code ``` python from vllm.entrypoints.llm import LLM from vllm.sampling_params import SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="google/gemma-2b") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ### 🐛 Describe the bug the error: Traceback (most recent call last): File "/home/hyp/testGemma.py", line 11, in llm = LLM(model="google/gemma-2b") File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 225, in from_engine_args engine_configs = engine_args.create_engine_configs() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/arg_utils.py", line...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:Failed that we generate the pompts with the google/gemma-2b model by the python code, bug;stale ### Your current environment ```text python 3.10.14 vllm 0.4.0.post1 vllm-nccl-cu12 2.18.1.0.1.0 ``` ### the python c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 8.1.0.1.0 ``` ### the python code ``` python from vllm.entrypoints.llm import LLM from vllm.sampling_params import SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ration_auto.py", line 1064, in from_pretrained config_class = CONFIG_MAPPING[config_dict["model_type"]] File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 761, in __getit...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]:Failed that we generate the pompts with the google/gemma-2b model by the python code, bug;stale ### Your current environment ```text python 3.10.14 vllm 0.4.0.post1 vllm-nccl-cu12 2.18.1.0.1.0 ``` ### the python c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: erate the pompts with the google/gemma-2b model by the python code, bug;stale ### Your current environment ```text python 3.10.14 vllm 0.4.0.post1 vllm-nccl-cu12 2.18.1.0.1.0 ``` ### the python code ``` python from vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
