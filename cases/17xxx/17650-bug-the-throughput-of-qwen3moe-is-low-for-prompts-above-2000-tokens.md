# vllm-project/vllm#17650: [Bug]: the throughput of qwen3moe is low for prompts above 2000 tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#17650](https://github.com/vllm-project/vllm/issues/17650) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: the throughput of qwen3moe is low for prompts above 2000 tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug this is my start script: ``` #!/bin/bash export CUDA_VISIBLE_DEVICES=2,3,4,5 export VLLM_ATTENTION_BACKEND=XFORMERS # export VLLM_USE_V1=1 source /usr/local/anaconda3/bin/activate /home/aabbccddwasd/.conda/envs/vllm-latest python -m vllm.entrypoints.openai.api_server \ --model /data-HV-1t/AI-stuff/qwen-models/Qwen3-30B-A3B \ --tensor-parallel-size=4 \ --enable-expert-parallel \ --gpu-memory-utilization 0.98 \ --max-model-len 32768 \ --enable-prefix-caching \ --served-model-name qwen3-30ba3b \ --swap-space 8 \ --disable-log-requests \ --dtype float16 \ --port 8000 \ ``` I found it can run up to about 75 tokens/s before 2000 token than suddenly drop to 10 tokens/s after 2000 token, at the same time, the utilization of one gpu drops to about 13%. could it be a problem with GPU communication? but why the speed drops so fast（suddenly from 75t/s to 10t/s） someone help me please ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_erro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: the throughput of qwen3moe is low for prompts above 2000 tokens bug;stale ### Your current environment ### 🐛 Describe the bug this is my start script: ``` #!/bin/bash export CUDA_VISIBLE_DEVICES=2,3,4,5 export VLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: `` #!/bin/bash export CUDA_VISIBLE_DEVICES=2,3,4,5 export VLLM_ATTENTION_BACKEND=XFORMERS # export VLLM_USE_V1=1 source /usr/local/anaconda3/bin/activate /home/aabbccddwasd/.conda/envs/vllm-latest python -m vllm.entrypo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e qwen3-30ba3b \ --swap-space 8 \ --disable-log-requests \ --dtype float16 \ --port 8000 \ ``` I found it can run up to about 75 tokens/s before 2000 token than suddenly drop to 10 tokens/s after 2000 token, at the same...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug this is my start script: ``` #!/bin/bash export CUDA_VISIBLE_DEVICES=2,3,4,5 export VLLM_ATTENTION_BACKEND=XFORMERS # export VLLM_USE_V1=1 source /usr/local/anaconda3/bin/activate /home/aabbccddwa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
