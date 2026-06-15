# vllm-project/vllm#16867: [Bug]: Bug while using deepspeed with TRL with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16867](https://github.com/vllm-project/vllm/issues/16867) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bug while using deepspeed with TRL with vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import datasets import functools from transformers import AutoModelForCausalLM from transformers import AutoTokenizer import trl from alpha.services.assistant.train import dataset from alpha.services.assistant.train import reward if __name__ == "__main__": processing_class = AutoTokenizer.from_pretrained('google/gemma-7b', padding_side="left") model = AutoModelForCausalLM.from_pretrained('google/gemma-7b') train_dataset = dataset.load_dataset(dataset.KnownClass(), datasets.Split.TRAIN) eval_dataset = dataset.load_dataset(dataset.KnownClass(), datasets.Split.VALIDATION) reward_fn: reward.SingleTurnComponentizedRewardFn = functools.partial( reward.stg_rewards, processing_class=processing_class, max_completion_length=5120 + 1536, ) config = trl.GRPOConfig( num_train_epochs=16, gradient_accumulation_steps=8, per_device_train_batch_size=16, per_device_eval_batch_size=16, num_generations=16, max_prompt_length=5120, max_completion_length=1536, use_cpu=False, beta=0.04, temperature=0.9, bf16=True, bf16_full_eval=True, torch_empty_cache_steps=1, eval_accumulation_steps=1 use_vllm=True, ) trainer = trl.GRPOTrainer( args=config, t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stale ### Your current environment ### 🐛 Describe the bug ```python import datasets import functools from transformers import AutoModelForCausalLM from transformers import AutoTokenizer import trl from alpha.services.as...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```python import datasets import functools from transformers import AutoModelForCausalLM from transformers import AutoTokenizer import trl from alpha.services.assistant.train import dataset from alpha.services.assistant...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nction: main mixed_precision: bf16 num_machines: 1 num_processes: 7 rdzv_backend: static same_network: true tpu_env: [] tpu_use_cluster: false tpu_use_sudo: false use_cpu: false ``` outputs: ``` Traceback (most recent c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: n() ``` Launching with: ``` export VLLM_USE_V1=0 export NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES=0 nohup trl vllm-serve --model google/gemma-3-4b-it --max-model-len 6656 --gpu-memory-utilization=0.9 --enable_prefix_caching...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Bug while using deepspeed with TRL with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug ```python import datasets import functools from transformers import AutoModelForCausalLM from transformer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
