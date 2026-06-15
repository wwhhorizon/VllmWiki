# vllm-project/vllm#12783: [Bug]: There is no module or parameter named '_orig_mod' in Qwen2ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#12783](https://github.com/vllm-project/vllm/issues/12783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: There is no module or parameter named '_orig_mod' in Qwen2ForCausalLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run the GRPO trainer example in Hugging Face TRL library: https://huggingface.co/docs/trl/main/en/grpo_trainer ```python # train_grpo.py from datasets import load_dataset from trl import GRPOConfig, GRPOTrainer dataset = load_dataset("trl-lib/tldr", split="train") # Define the reward function, which rewards completions that are close to 20 characters def reward_len(completions, **kwargs): return [abs(20 - len(completion)) for completion in completions] training_args = GRPOConfig(output_dir="Qwen2-0.5B-GRPO", logging_steps=10, use_vllm=True, vllm_device="cuda:0", vllm_gpu_memory_utilization=0.3) trainer = GRPOTrainer( model="Qwen/Qwen2-0.5B-Instruct", reward_funcs=reward_len, args=training_args, train_dataset=dataset, ) trainer.train() ``` It works when not using vllm (i.e. when use_vllm=False) But when I use vllm, I get the following error: ``` ValueError: There is no module or parameter named '_orig_mod' in Qwen2ForCausalLM ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://do...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: o/docs/trl/main/en/grpo_trainer ```python # train_grpo.py from datasets import load_dataset from trl import GRPOConfig, GRPOTrainer dataset = load_dataset("trl-lib/tldr", split="train") # Define the reward function, whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: There is no module or parameter named '_orig_mod' in Qwen2ForCausalLM bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run the GRPO trainer example in Hugging Face TRL library: https:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: put_dir="Qwen2-0.5B-GRPO", logging_steps=10, use_vllm=True, vllm_device="cuda:0", vllm_gpu_memory_utilization=0.3) trainer = GRPOTrainer( model="Qwen/Qwen2-0.5B-Instruct", reward_funcs=reward_len, args=training_args, tr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: trainer.train() ``` It works when not using vllm (i.e. when use_vllm=False) But when I use vllm, I get the following error: ``` ValueError: There is no module or parameter named '_orig_mod' in Qwen2ForCausalLM ``` ### B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
