# vllm-project/vllm#789: Error reported when running multiple cards with docker container on cloud platform

| 字段 | 值 |
| --- | --- |
| Issue | [#789](https://github.com/vllm-project/vllm/issues/789) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error reported when running multiple cards with docker container on cloud platform

### Issue 正文摘录

WARNING 08-18 01:35:48 tokenizer.py:63] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. (RayWorker pid=4711) *** SIGBUS received at time=1692322557 on cpu 5 *** (RayWorker pid=4711) PC: @ 0x7fca7c80cb41 (unknown) (unknown) (RayWorker pid=4711) @ 0x7fca7c9e1420 3424 (unknown) (RayWorker pid=4711) @ 0x554b2d6c63636e2f (unknown) (unknown) (RayWorker pid=4711) [2023-08-18 01:35:57,940 E 4711 4962] logging.cc:361: *** SIGBUS received at time=1692322557 on cpu 5 *** (RayWorker pid=4711) [2023-08-18 01:35:57,941 E 4711 4962] logging.cc:361: PC: @ 0x7fca7c80cb41 (unknown) (unknown) (RayWorker pid=4711) [2023-08-18 01:35:57,941 E 4711 4962] logging.cc:361: @ 0x7fca7c9e1420 3424 (unknown) (RayWorker pid=4711) [2023-08-18 01:35:57,943 E 4711 4962] logging.cc:361: @ 0x554b2d6c63636e2f (unknown) (unknown) (RayWorker pid=4711) Fatal Python error: Bus error (RayWorker pid=4711) (RayWorker pid=4711) (RayWorker pid=4711) Extension modules: msgpack._cmsgpack, setproctitle, google._upb._message, psutil._psutil_linux, psutil._psutil_posix, yaml._yaml, grpc._cython.cygrpc, ray._raylet, charset_normalizer.md, numpy.core._multiarray_umath, numpy....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Error reported when running multiple cards with docker container on cloud platform WARNING 08-18 01:35:48 tokenizer.py:63] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: as._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.lib, pandas._libs.hashing, pandas....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: sfs, pyarrow._s3fs, pandas._libs.tslibs.np_datetime, pandas._libs.tslibs.dtypes, pandas._libs.tslibs.base, pandas._libs.tslibs.nattype, pandas._libs.tslibs.timezones, pandas._libs.tslibs.ccalendar, pandas._libs.tslibs.f...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: te-packages/vllm/engine/llm_engine.py", line 182, in _init_cache num_blocks = self._run_workers( File "/usr/local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 474, in _run_workers all_outputs = ray.get(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
