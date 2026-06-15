# vllm-project/vllm#28390: [Bug]: vllm 0.11.0 RuntimeError: The size of tensor a (768) must match the size of tensor b (797)

| 字段 | 值 |
| --- | --- |
| Issue | [#28390](https://github.com/vllm-project/vllm/issues/28390) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.11.0 RuntimeError: The size of tensor a (768) must match the size of tensor b (797)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In verl 0.7.0, run the script ``` PYTHONUNBUFFERED=1 python3 -m verl.trainer.main_ppo \ data.train_files=/data/student007/verl/data/gsm8k/train.parquet \ data.val_files=/data/student007/verl/data/gsm8k/test.parquet \ data.train_batch_size=256 \ data.max_prompt_length=512 \ data.max_response_length=256 \ actor_rollout_ref.model.path=Qwen/Qwen2.5-0.5B-Instruct \ actor_rollout_ref.actor.optim.lr=1e-6 \ actor_rollout_ref.actor.ppo_mini_batch_size=64 \ actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=4 \ actor_rollout_ref.rollout.name=vllm \ actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=8 \ actor_rollout_ref.rollout.tensor_model_parallel_size=1 \ actor_rollout_ref.rollout.gpu_memory_utilization=0.4 \ actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=4 \ actor_rollout_ref.rollout.max_num_seqs=1024 \ critic.optim.lr=1e-5 \ critic.model.path=Qwen/Qwen2.5-0.5B-Instruct \ critic.ppo_micro_batch_size_per_gpu=4 \ algorithm.kl_ctrl.kl_coef=0.001 \ trainer.logger=wandb \ trainer.val_before_train=False \ trainer.n_gpus_per_node=1 \ trainer.nnodes=1 \ trainer.save_freq=100 \ trainer.test_freq=10 \ trainer.total_epochs=15...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -m verl.trainer.main_ppo \ data.train_files=/data/student007/verl/data/gsm8k/train.parquet \ data.val_files=/data/student007/verl/data/gsm8k/test.parquet \ data.train_batch_size=256 \ data.max_prompt_length=512 \ data.m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: on dimension 0 ``` More error message: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 0%| | 0/67 [00:00<?, ?it/s] Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 4%|▍ | 3/67 [00:00<00:02, 25.94it/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: x_prompt_length=512 \ data.max_response_length=256 \ actor_rollout_ref.model.path=Qwen/Qwen2.5-0.5B-Instruct \ actor_rollout_ref.actor.optim.lr=1e-6 \ actor_rollout_ref.actor.ppo_mini_batch_size=64 \ actor_rollout_ref.a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: a/gsm8k/train.parquet \ data.val_files=/data/student007/verl/data/gsm8k/test.parquet \ data.train_batch_size=256 \ data.max_prompt_length=512 \ data.max_response_length=256 \ actor_rollout_ref.model.path=Qwen/Qwen2.5-0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
