# vllm-project/vllm#14449: [Bug]: `vllm serve Qwen/QwQ-32B-AWQ  --tensor-parallel-size 2` hangs with both RTX A6000 GPUs at max utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#14449](https://github.com/vllm-project/vllm/issues/14449) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `vllm serve Qwen/QwQ-32B-AWQ  --tensor-parallel-size 2` hangs with both RTX A6000 GPUs at max utilization

### Issue 正文摘录

## tl;dr; Using `--tensor-parallel-size 2` hangs with both GPUs at 100% utilization and no debug logs explaining anything. ## Details I know all the devs are hyper-focused on `R1` optimizations right now, which I appreciate. Just dropping this here for when there is time and for anyone else rushing to get [Qwen/QwQ-32B](https://huggingface.co/Qwen/QwQ-32B/discussions/11) running right now. The AWQ quant runs fine on a single A6000 GPU like so: ``` # https://docs.astral.sh/uv/getting-started/installation/ curl -LsSf https://astral.sh/uv/install.sh | sh # https://docs.vllm.ai/en/stable/getting_started/quickstart.html mkdir vllm cd vllm/ uv venv ./venv --python=3.12 --python-preference=only-managed source venv/bin/activate uv pip install vllm vllm --version # INFO 03-07 11:13:15 __init__.py:207] Automatically detected platform cuda. # 0.7.3 # 1x GPU works good! OMP_NUM_THREADS=1 \ PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve \ Qwen/QwQ-32B-AWQ \ --download-dir /mnt/raid/models/ \ --load-format auto \ --dtype auto \ --kv-cache-dtype auto \ --max-model-len 32768 \ --host 127.0.0.1 \ --port 8080 # VRAM 35.46GiB / 47.99GiB # INFO 03-07 11:41:10 metrics.py:455] Avg prompt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: the devs are hyper-focused on `R1` optimizations right now, which I appreciate. Just dropping this here for when there is time and for anyone else rushing to get [Qwen/QwQ-32B](https://huggingface.co/Qwen/QwQ-32B/discus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `vllm serve Qwen/QwQ-32B-AWQ --tensor-parallel-size 2` hangs with both RTX A6000 GPUs at max utilization bug;stale ## tl;dr; Using `--tensor-parallel-size 2` hangs with both GPUs at 100% utilization and no debug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: `vllm serve Qwen/QwQ-32B-AWQ --tensor-parallel-size 2` hangs with both RTX A6000 GPUs at max utilization bug;stale ## tl;dr; Using `--tensor-parallel-size 2` hangs with both GPUs at 100% utilization and no debug logs ex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: /huggingface.co/Qwen/QwQ-32B/discussions/11) running right now. The AWQ quant runs fine on a single A6000 GPU like so: ``` # https://docs.astral.sh/uv/getting-started/installation/ curl -LsSf https://astral.sh/uv/instal...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ir /mnt/raid/models/ \ --load-format auto \ --dtype auto \ --kv-cache-dtype auto \ --max-model-len 32768 \ --host 127.0.0.1 \ --port 8080 # VRAM 35.46GiB / 47.99GiB # INFO 03-07 11:41:10 metrics.py:455] Avg prompt throu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
