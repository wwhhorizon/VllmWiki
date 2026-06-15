# vllm-project/vllm#41691: [Bug]: The last few reasoning output tokens are missing when using Gemma4 and setting "--streaming-interval" to be larger than 1

| 字段 | 值 |
| --- | --- |
| Issue | [#41691](https://github.com/vllm-project/vllm/issues/41691) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The last few reasoning output tokens are missing when using Gemma4 and setting "--streaming-interval" to be larger than 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When hosting Gemma4-31B-it on vLLM 0.20.0 with `--streaming-interval` larger than 1 and invoking the model in streaming mode, the last few reasoning output tokens are missing. Script to launch the vLLM server: ```bash nohup vllm serve ./Gemma4-31B-it \ --served-model-name "gemma4-31b-it" \ --api-key \ --host 0.0.0.0 \ --port \ --max-model-len 262144 \ --max-num-seqs 128 \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.90 \ --stream-interval 10 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --async-scheduling \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ > "$log_file" 2>&1 & ``` Script to demonstrate the bug: ```python import os from openai import OpenAI API_BASE = "http://jb-aionlineinferenceservice-155859607233257216-8000-nhss-job.z2120.nhss.zhejianglab.com:31080/v1" API_KEY = os.environ['GEMMA4_API_KEY'] MODEL = "gemma4-31b-it" client = OpenAI( base_url = API_BASE, api_key = API_KEY, ) #%% Streaming mode stream = client.chat.completions.create( model = MODEL, messages = [ {"role": "user", "content": "A snail is at the bottom of a 20-foot well. Each day it climbs 3 fee...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: > "$log_file" 2>&1 & ``` Script to demonstrate the bug: ```python import os from openai import OpenAI API_BASE = "http://jb-aionlineinferenceservice-155859607233257216-8000-nhss-job.z2120.nhss.zhejianglab.com:31080/v1"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: emory-utilization 0.90 \ --stream-interval 10 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --async-scheduling \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ > "$log...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The last few reasoning output tokens are missing when using Gemma4 and setting "--streaming-interval" to be larger than 1 bug ### Your current environment ### 🐛 Describe the bug When hosting Gemma4-31B-it on vLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
