# vllm-project/vllm#13497: [Usage]: vLLM and In the fly tool calling

| 字段 | 值 |
| --- | --- |
| Issue | [#13497](https://github.com/vllm-project/vllm/issues/13497) |
| 状态 | closed |
| 标签 | usage;stale;tool-calling |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM and In the fly tool calling

### Issue 正文摘录

### Your current environment Hey, I was wondering if VLLM support tooling calls in a specific way. Let s say i want the completion to depends on the output of my tool calling . Does vLLM support that ? to do so it needs to have access to that function but there is no includes in the vllm command of the functions .. so how would it use them ? Let say using the same example of get_weather, i have a prompt as follow : ``` # Instructions : Using this categories, give an answer about what to do in a city today. if the temperature is above 25 : go out for a tour if the temperature is betwen 15 and 25 : visit friends if temperature bellow 15 : stay home you can use functions and api calls if some information are needed. # Question : What to do today in Texas ? go for a tour, stay home or stay visit friends ? ``` basically the model needs to call for get_weather, get the output then response . can vllm automatically handle this ? in the sense that it stops the generation wait for get_weather execution, insert it and then use it in the context. Thank you ```text The output of `python collect_env.py` INFO 02-18 21:25:53 __init__.py:190] Automatically detected platform cuda. Collecting envir...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: environment Hey, I was wondering if VLLM support tooling calls in a specific way. Let s say i want the completion to depends on the output of my tool calling . Does vLLM support that ? to do so it needs to have access t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: py` INFO 02-18 21:25:53 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ure bellow 15 : stay home you can use functions and api calls if some information are needed. # Question : What to do today in Texas ? go for a tour, stay home or stay visit friends ? ``` basically the model needs to ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: vLLM and In the fly tool calling usage;stale;tool-calling ### Your current environment Hey, I was wondering if VLLM support tooling calls in a specific way. Let s say i want the completion to depends on the out...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u121 [pip3] torchvision==0.20.1+cu121 [pip3] transformers==4.49.0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.2 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
