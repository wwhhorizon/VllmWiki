# vllm-project/vllm#8421: [Bug]: mismatch between multimodal tokens and placeholders for Llava-Next (4 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#8421](https://github.com/vllm-project/vllm/issues/8421) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mismatch between multimodal tokens and placeholders for Llava-Next (4 GPUs)

### Issue 正文摘录

### Your current environment Running my original script through SLURM so that is why the output above doesn't have any GPUs. I am on 4 H100s. ### Model Input Dumps _No response_ ### 🐛 Describe the bug Similar to https://github.com/vllm-project/vllm/issues/7996, I am running into when using [Llava-NexT](https://huggingface.co/llava-hf/llava-v1.6-mistral-7b-hf): ``` [rank0]: ValueError: Attempted to assign 2340 + 2144 + 1850 + 2160 + 2832 + 2438 + 2340 + 2830 + 2536 + 1948 = 23418 multimodal tokens to 23516 placeholders ``` All the code is here: https://github.com/sayakpaul/simple-image-recaptioning This is why I launch it: ```bash # full CC3M training set python main.py \ --data_path="pipe:curl -s -f -L https://huggingface.co/datasets/pixparse/cc3m-wds/resolve/main/cc3m-train-{0000..0575}.tar" --batch_size=48 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: mismatch between multimodal tokens and placeholders for Llava-Next (4 GPUs) bug ### Your current environment Running my original script through SLURM so that is why the output above doesn't have any GPUs. I am on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: mismatch between multimodal tokens and placeholders for Llava-Next (4 GPUs) bug ### Your current environment Running my original script through SLURM so that is why the output above doesn't have any GPUs. I am on...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: mismatch between multimodal tokens and placeholders for Llava-Next (4 GPUs) bug ### Your current environment Running my original script through SLURM so that is why the output above doesn't have any GPUs. I am on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
