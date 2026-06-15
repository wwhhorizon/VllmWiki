# vllm-project/vllm#28118: [Bug]: vllm version error about Ascend NPU

| 字段 | 值 |
| --- | --- |
| Issue | [#28118](https://github.com/vllm-project/vllm/issues/28118) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm version error about Ascend NPU

### Issue 正文摘录

### Your current environment i try to run vllm+npu training script: examples/sglang_multiturn/run_qwen2.5-3b_gsm8k_multiturn_vllm_fsdp.sh ``` # run on Ascend 910 # make sure your current working directory is the root of the project set -x ulimit -n 65535 #set vllm v1 env export VLLM_USE_V1=1 PROJECT_DIR="$(pwd)" CONFIG_PATH="$PROJECT_DIR/examples/sglang_multiturn/config" TRAIN_BATCH_SIZE=32 MICRO_BATCH_SIZE=8 python3 -m verl.trainer.main_ppo \ --config-path="$CONFIG_PATH" \ --config-name='gsm8k_multiturn_grpo' \ actor_rollout_ref.rollout.name=vllm \ algorithm.adv_estimator=grpo \ data.train_batch_size=${TRAIN_BATCH_SIZE} \ data.max_prompt_length=1024 \ data.max_response_length=1024 \ data.filter_overlong_prompts=True \ data.truncation='error' \ data.return_raw_chat=True \ actor_rollout_ref.model.path="/home/Qwen2.5-3B-Instruct" \ actor_rollout_ref.actor.optim.lr=1e-6 \ actor_rollout_ref.actor.ppo_mini_batch_size=${TRAIN_BATCH_SIZE} \ actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=${MICRO_BATCH_SIZE} \ actor_rollout_ref.actor.use_kl_loss=True \ actor_rollout_ref.actor.kl_loss_coef=0.001 \ actor_rollout_ref.actor.kl_loss_type=low_var_kl \ actor_rollout_ref.actor.entropy_coeff=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt i try to run vllm+npu training script: examples/sglang_multiturn/run_qwen2.5-3b_gsm8k_multiturn_vllm_fsdp.sh ``` # run on Ascend 910 # make sure your current working directory is the root of the project set -x ulimit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: vllm version error about Ascend NPU bug ### Your current environment i try to run vllm+npu training script: examples/sglang_multiturn/run_qwen2.5-3b_gsm8k_multiturn_vllm_fsdp.sh ``` # run on Ascend 910 # make sur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: run vllm+npu training script: examples/sglang_multiturn/run_qwen2.5-3b_gsm8k_multiturn_vllm_fsdp.sh ``` # run on Ascend 910 # make sure your current working directory is the root of the project set -x ulimit -n 65535 #s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: atch_size_per_gpu=${MICRO_BATCH_SIZE} \ algorithm.use_kl_in_reward=False \ trainer.critic_warmup=0 \ trainer.project_name='gsm8k_async_rl' \ trainer.experiment_name='qwen2.5-3b_function_rm-gsm8k-sgl-multi-w-tool-verify-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: _async_server.py", line 549, in sleep await self.servers[0].wait_for_requests_to_drain.remote() ray.exceptions.RayTaskError(AttributeError): ray::vLLMHttpServer.wait_for_requests_to_drain() (pid=324161, ip=10.1.68.108,...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
