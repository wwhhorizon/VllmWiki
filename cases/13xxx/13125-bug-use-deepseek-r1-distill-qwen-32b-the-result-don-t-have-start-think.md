# vllm-project/vllm#13125: [Bug]: Use DeepSeek-R1-Distill-Qwen-32B, the result don't have start <think>  and can not parse reasoning_content.

| 字段 | 值 |
| --- | --- |
| Issue | [#13125](https://github.com/vllm-project/vllm/issues/13125) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Use DeepSeek-R1-Distill-Qwen-32B, the result don't have start <think>  and can not parse reasoning_content.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Use DeepSeek-R1-Distill-Qwen-32B, the result don't have start and can not parse reasoning_content. '''bash CUDA_VISIBLE_DEVICES=0 nohup \ python -m vllm.entrypoints.openai.api_server \ --model /data/models/DeepSeek-R1-Distill-Qwen-32B/ \ --trust-remote-code \ --served-model-name deepseek-32b \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.80 \ --max-model-len 3000 \ --dtype bfloat16 \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --enforce-eager \ --port 10009 >log_vllm_deepseek32b.log 2>&1 & ''' Then, curl {"model":"deepseek-32b","stream": false,"top_k":-1,"top_p": 0.95,"temperature": 0.6,"repetition_penalty": 1.0,"messages": [{"role": "user", "content": "我想买猫粮，预算2000"}]} Result: ![Image](https://github.com/user-attachments/assets/bb82a60f-4e81-4a86-92f8-4a90d82c4d68) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rallel-size 1 \ --gpu-memory-utilization 0.80 \ --max-model-len 3000 \ --dtype bfloat16 \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --enforce-eager \ --port 10009 >log_vllm_deepseek32b.log 2>&1 & ''' Then, c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: result don't have start and can not parse reasoning_content. '''bash CUDA_VISIBLE_DEVICES=0 nohup \ python -m vllm.entrypoints.openai.api_server \ --model /data/models/DeepSeek-R1-Distill-Qwen-32B/ \ --trust-remote-code...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Use DeepSeek-R1-Distill-Qwen-32B, the result don't have start <think> and can not parse reasoning_content. bug ### Your current environment ### 🐛 Describe the bug Use DeepSeek-R1-Distill-Qwen-32B, the result don'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
