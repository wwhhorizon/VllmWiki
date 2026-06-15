# vllm-project/vllm#22008: [Installation]: with latest vllm source code installation done, but failed to run vllm server

| 字段 | 值 |
| --- | --- |
| Issue | [#22008](https://github.com/vllm-project/vllm/issues/22008) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: with latest vllm source code installation done, but failed to run vllm server

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` server is hang now ### How you are installing vllm ```sh pip install -e . inside source code ``` the error log is here. it said flashinfer failed to find C++ math.h, but I am pretty sure the file is there by ls ``` (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] The above exception was the direct cause of the following exception: (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] Traceback (most recent call last): (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] File "/mnt/nvme1n1/wayne/vast/vast/vllm/vllm/v1/executor/multiproc_executor.py", line 589, in worker_busy_loop (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] output = func(*args, **kwargs) (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] File...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: with latest vllm source code installation done, but failed to run vllm server installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` server is hang now ### How
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vast/vllm/vllm/v1/sample/ops/topk_topp_sampler.py", line 108, in forward_cuda (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] return flashinfer_sample(logits.contiguous(), k, p, generators...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 5 [multiproc_executor.py:594] sampled = self.sample(logits, sampling_metadata) (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multiproc_executor.py:594] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=0 pid...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: h pip install -e . inside source code ``` the error log is here. it said flashinfer failed to find C++ math.h, but I am pretty sure the file is there by ls ``` (VllmWorker rank=0 pid=71558) ERROR 07-31 08:44:05 [multipr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: --threads=32 -use_fast_math -DFLASHINFER_ENABLE_F16 -DFLASHINFER_ENABLE_BF16 -DFLASHINFER_ENABLE_FP8_E4M3 -DFLASHINFER_ENABLE_FP8_E5M2 -DNDEBUG -c /mnt/nvme1n1/wayne/vast/vast/lib/python3.12/site-packages/flashinfer/dat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
