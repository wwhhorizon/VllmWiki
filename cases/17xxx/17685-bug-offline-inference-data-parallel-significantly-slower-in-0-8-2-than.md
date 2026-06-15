# vllm-project/vllm#17685: [Bug]: Offline inference data parallel significantly slower in 0.8.2 than 0.6.4.post1 and 0.7.2

| 字段 | 值 |
| --- | --- |
| Issue | [#17685](https://github.com/vllm-project/vllm/issues/17685) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Offline inference data parallel significantly slower in 0.8.2 than 0.6.4.post1 and 0.7.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi everyone, we are running offline inference with Llama 3.1 8B Instruct AWQ on the same dataset with the same command (parameters) with a g5.12xlarge instance from AWS. After upgrading from v0.6.4.post1 to v0.8.2, we observed the run time is significantly longer with v0.8.2 at 1 hour vs v0.6.4.post1 at only 20 minutes. **_We also tested v0.7.2 and found the performance is similar as v0.6.4.post1, at about 20 minutes._** We checked GPU utilization and found v0.8.2's GPU utilization is unstable which fluctuates between 0%-100% while v0.6.4.post1's utilization sustains at 95%-100%. So far we have tried disabling NCCL, using V0 engine instead of V1, and setting VLLM_ENABLE_V1_MULTIPROCESSING as 1 vs 0. None has helped to return the performance to normal. It's important to note v0.6.4.post1 and v0.7.2 both initialize V0 engine whereas for 0.8.2 we tried both V0 and V1 neither performed well. We did try the single GPU instance g5.4xlarge with v0.8.2 and observed GPU utilization as expected sustaining at around 100% so we guess data parallel offline inference with multi-gpu is not functioning properly in this case. We are using the dat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ING as 1 vs 0. None has helped to return the performance to normal. It's important to note v0.6.4.post1 and v0.7.2 both initialize V0 engine whereas for 0.8.2 we tried both V0 and V1 neither performed well. We did try t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: th}") lora_request = LoRARequest("from_args", 1, lora_path) else: lora_request = None outputs = llm.chat(prompts, sampling_params, lora_request=lora_request) return requests_batched, outputs # here is the main parallel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ta parallel significantly slower in 0.8.2 than 0.6.4.post1 and 0.7.2 bug;stale ### Your current environment ### 🐛 Describe the bug Hi everyone, we are running offline inference with Llama 3.1 8B Instruct AWQ on the same...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: os.environ["VLLM_DP_MASTER_PORT"] = str(dp_master_port) os.environ["CUDA_VISIBLE_DEVICES"] = ",".join( str(i) for i in range(dp_rank * gpus_per_dp_rank, (dp_rank + 1) * gpus_per_dp_rank)) requests_batched = vllm_io.batc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # 🐛 Describe the bug Hi everyone, we are running offline inference with Llama 3.1 8B Instruct AWQ on the same dataset with the same command (parameters) with a g5.12xlarge instance from AWS. After upgrading from v0.6.4....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
