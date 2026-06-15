# vllm-project/vllm#20895: [Bug]: Gemma3 can not be launched in vllm CLI

| 字段 | 值 |
| --- | --- |
| Issue | [#20895](https://github.com/vllm-project/vllm/issues/20895) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 can not be launched in vllm CLI

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash VLLM_USE_V1=0 vllm serve google/gemma-3-27b-it \ --port 8885 \ --dtype bfloat16 --tensor-parallel-size 2 --gpu-memory-utilization 0.95 \ --max-model-len 131072 \ --limit-mm-per-prompt image=34 ``` The above vllm CLI commend fail to launch, the error message is arranged at the end (i can not findout the issue for reviewing the error message though). On the other hand, i can applied the identical env to launch gemma3-12b-it via llama-factory (python client). In the backend, llamafactory calls : ```python from vllm import AsyncEngineArgs, AsyncLLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARequest ``` successful launched : #### vllm CLI Error message : ``` INFO 07-13 19:22:18 [__init__.py:239] Automatically detected platform cuda. [104/1876] INFO 07-13 19:22:23 [api_server.py:1043] vLLM API server version 0.8.5 INFO 07-13 19:22:23 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='google/gemma-3-27b-it' ...omit args INFO 07-13 19:22:24 [config.py:2968] Downcasting torch.float32 to torch.bfloat16. INFO 07-13 19:22:34 [config.py:717] This model supports multiple tasks: {'embed', 'cla...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Gemma3 can not be launched in vllm CLI bug ### Your current environment ### 🐛 Describe the bug ```bash VLLM_USE_V1=0 vllm serve google/gemma-3-27b-it \ --port 8885 \ --dtype bfloat16 --tensor-parallel-size 2
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ython client). In the backend, llamafactory calls : ```python from vllm import AsyncEngineArgs, AsyncLLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARequest ``` successful launched : #### vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: VLLM_USE_V1=0 vllm serve google/gemma-3-27b-it \ --port 8885 \ --dtype bfloat16 --tensor-parallel-size 2 --gpu-memory-utilization 0.95 \ --max-model-len 131072 \ --limit-mm-per-prompt image=34 ``` The above vllm CLI com...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ory calls : ```python from vllm import AsyncEngineArgs, AsyncLLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARequest ``` successful launched : #### vllm CLI Error message : ``` INFO 07-13 19:2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: al env to launch gemma3-12b-it via llama-factory (python client). In the backend, llamafactory calls : ```python from vllm import AsyncEngineArgs, AsyncLLMEngine, RequestOutput, SamplingParams from vllm.lora.request imp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
