# vllm-project/vllm#24580: [Bug]: crash on startup with TP>1 on H100 nodes: AttributeError in ShmRingBuffer.shared_memory

| 字段 | 值 |
| --- | --- |
| Issue | [#24580](https://github.com/vllm-project/vllm/issues/24580) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: crash on startup with TP>1 on H100 nodes: AttributeError in ShmRingBuffer.shared_memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM with tensor-parallel size > 1 on nodes with multiple H100s, some models reliably crash during engine startup with: ``` AttributeError: 'ShmRingBuffer' object has no attribute 'shared_memory' ``` This appears to stem from the multiprocessing message-queue broadcaster using POSIX shared memory. Logs show reader workers failing to attach to the shared memory segment created by the writer; later the reader crashes while accessing `self.shared_memory`. ### Affected models - Consistent repro: `zai-org/GLM-4.5-Air` (BF16) with `--tensor-parallel-size 8` - Also seen previously: `Qwen/QwQ-32B` with `--tensor-parallel-size 4` ### Minimal repro (GLM-4.5-Air BF16) - Slurm command (debug partition, 8 GPUs): ```bash srun --partition=debug --nodes=1 --ntasks=1 --gres=gpu:8 --cpus-per-task=16 --mem=128G --time=40 \ bash -lc 'cd /fsx/sander/project; \ PORT=$(shuf -i 20000-29999 -n1); \ timeout 1200 uv run vllm serve zai-org/GLM-4.5-Air \ --port $PORT \ --tensor-parallel-size 8 \ --max-model-len 65536 \ --gpu-memory-utilization 0.9 \ --reasoning-parser glm45 \ --tool-call-parser glm45 \ --enable-auto-tool-choice \ --max-num-batch...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: crash on startup with TP>1 on H100 nodes: AttributeError in ShmRingBuffer.shared_memory bug;stale ### Your current environment ### 🐛 Describe the bug When running vLLM with tensor-parallel size > 1 on nodes with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ] No such file or directory ... ``` ### Suspected cause Race or env-specific failure in creating/propagating the POSIX SHM name across TP worker processes on H100 nodes. The code suppresses FileNotFoundError when deseri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: th TP>1 on H100 nodes: AttributeError in ShmRingBuffer.shared_memory bug;stale ### Your current environment ### 🐛 Describe the bug When running vLLM with tensor-parallel size > 1 on nodes with multiple H100s, some model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: emory`. ### Affected models - Consistent repro: `zai-org/GLM-4.5-Air` (BF16) with `--tensor-parallel-size 8` - Also seen previously: `Qwen/QwQ-32B` with `--tensor-parallel-size 4` ### Minimal repro (GLM-4.5-Air BF16) -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng vLLM with tensor-parallel size > 1 on nodes with multiple H100s, some models reliably crash during engine startup with: ``` AttributeError: 'ShmRingBuffer' object has no attribute 'shared_memory' ``` This appears to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
