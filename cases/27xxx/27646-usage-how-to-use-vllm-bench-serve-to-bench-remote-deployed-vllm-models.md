# vllm-project/vllm#27646: [Usage]: How to use vllm bench serve to bench remote deployed vllm models (can't bench when ep enabled!!!)

| 字段 | 值 |
| --- | --- |
| Issue | [#27646](https://github.com/vllm-project/vllm/issues/27646) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use vllm bench serve to bench remote deployed vllm models (can't bench when ep enabled!!!)

### Issue 正文摘录

### Your current environment I deployed dpskv3 in a remote server using: ``` export VLLM_USE_V1=1 export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve /models/hf/models--deepseek-ai--DeepSeek-V3 --tensor-parallel-size 1 --data-parallel-size 8 --enable-expert-parallel --no-enforce-eager --load-format dummy ``` And on another server: ``` VLLM_USE_V1=1 vllm bench serve --model /models/hf/models--deepseek-ai--DeepSeek-V3/ --endpoint /v1/completions --dataset-name sharegpt --dataset-path /datasets/ShareGPT/ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 10 --ready-check-timeout-sec 0 --ip 10.102.212.22 --port 8000 ``` where 10.102.212.22 is the server ip， 8000 is the default port And I got this below error on server: ``` "POST /v1/completions HTTP/1.1" 404 Not Found ``` ### How would you like to use vllm I want to run inference of a deepseekv3. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to use vllm bench serve to bench remote deployed vllm models (can't bench when ep enabled!!!) usage;stale ### Your current environment I deployed dpskv3 in a remote server using: ``` export VLLM_USE_V1=1 ex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r using: ``` export VLLM_USE_V1=1 export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve /models/hf/models--deepseek-ai--DeepSeek-V3 --tensor-parallel-size 1 --data-parallel-size 8 --enable-expert-parallel --no-enfor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 3 in a remote server using: ``` export VLLM_USE_V1=1 export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve /models/hf/models--deepseek-ai--DeepSeek-V3 --tensor-parallel-size 1 --data-parallel-size 8 --enable-expert-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: v3. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ai--DeepSeek-V3 --tensor-parallel-size 1 --data-parallel-size 8 --enable-expert-parallel --no-enforce-eager --load-format dummy ``` And on another server: ``` VLLM_USE_V1=1 vllm bench serve --model /models/hf/models--de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
