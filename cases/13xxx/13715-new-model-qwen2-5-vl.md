# vllm-project/vllm#13715: [New Model]: Qwen2.5-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#13715](https://github.com/vllm-project/vllm/issues/13715) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Qwen2.5-VL

### Issue 正文摘录

### The model to consider. It looks like vllm doesn't currently support Qwen 2.5-VL? ray.exceptions.RayTaskError(ValueError): ray::WorkerDict.actor_rollout_generate_sequences() (pid=67366, ip=192.168.128.5, actor_id=2681de9b19487eb6c57dea4401000000, repr= ) File "/mnt/2050data/wentao.zhang/MultiModalMath/verl/single_controller/ray/base.py", line 399, in func return getattr(self.worker_dict[key], name)(*args, **kwargs) File "/mnt/2050data/wentao.zhang/MultiModalMath/verl/single_controller/base/decorator.py", line 404, in inner return func(*args, **kwargs) File "/mnt/2050data/wentao.zhang/MultiModalMath/verl/workers/fsdp_workers.py", line 463, in generate_sequences with self.rollout_sharding_manager: File "/mnt/2050data/wentao.zhang/MultiModalMath/verl/workers/sharding_manager/fsdp_vllm.py", line 83, in __enter__ load_dtensor_weights( File "/mnt/2050data/wentao.zhang/MultiModalMath/verl/third_party/vllm/vllm_spmd/dtensor_weight_loaders.py", line 364, in load_dtensor_weights weight_loader = _get_model_weight_loader(vllm_model.__class__.__name__) File "/mnt/2050data/wentao.zhang/MultiModalMath/verl/third_party/vllm/vllm_spmd/dtensor_weight_loaders.py", line 374, in _get_model_weight_l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Qwen2.5-VL new-model ### The model to consider. It looks like vllm doesn't currently support Qwen 2.5-VL? ray.exceptions.RayTaskError(ValueError): ray::WorkerDict.actor_rollout_generate_sequences() (pid=673...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .py", line 374, in _get_model_weight_loader raise ValueError(f"Model architectures {arch} are not supported for now. " ValueError: Model architectures Qwen2_5_VLForConditionalGeneration are not supported for now. Suppor...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nLMForCausalLM', 'AquilaModel', 'AquilaForCausalLM', 'Phi3ForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPTBigCodeForCausalLM', 'Starcoder2ForCausalLM', 'Qwen2ForCausalLM', 'DeepseekV2ForCausalLM', 'Qwen2VLFor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
