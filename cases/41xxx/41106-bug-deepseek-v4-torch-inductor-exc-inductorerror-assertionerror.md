# vllm-project/vllm#41106: [Bug] Deepseek v4 :torch._inductor.exc.InductorError: AssertionError:

| 字段 | 值 |
| --- | --- |
| Issue | [#41106](https://github.com/vllm-project/vllm/issues/41106) |
| 状态 | closed |
| 标签 | bug;DSv4 |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;moe;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Deepseek v4 :torch._inductor.exc.InductorError: AssertionError:

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When launching deepseek v4 with tp8 on H100, encountered the following error: ``` WorkerProc hit an exception. (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] Traceback (most recent call last): (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] output = func(*args, **kwargs) (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 124, in decorate_context (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] return func(*args, **kwargs) (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_wo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] self.aot_compiled_fn = self.aot_compile(*args, **kwargs) (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm serve /mnt/model/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --data-parallel-size 1 --tensor-parallel-size 8 --compilation-config '{"cudagraph_mode":"FULL_AND_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nment ### 🐛 Describe the bug When launching deepseek v4 with tp8 on H100, encountered the following error: ``` WorkerProc hit an exception. (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] Tra...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: match.replace_by_example(decomp, flat_args, run_functional_passes=False) (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/torch/_inductor/pattern_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 04-28 06:25:58 [multiproc_executor.py:962] self.model_runner.profile_run() (Worker_TP6_EP6 pid=13431) ERROR 04-28 06:25:58 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
