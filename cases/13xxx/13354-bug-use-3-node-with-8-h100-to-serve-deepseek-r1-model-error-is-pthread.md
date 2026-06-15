# vllm-project/vllm#13354: [Bug]: Use 3 node with 8*H100 to serve Deepseek R1 model, error is   pthread_create failed: Resource temporarily unavailable

| 字段 | 值 |
| --- | --- |
| Issue | [#13354](https://github.com/vllm-project/vllm/issues/13354) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Use 3 node with 8*H100 to serve Deepseek R1 model, error is   pthread_create failed: Resource temporarily unavailable

### Issue 正文摘录

### Your current environment root@vllm-worker-6dd66f997f-pj6g4:~# **ulimit -a** real-time non-blocking time (microseconds, -R) unlimited core file size (blocks, -c) unlimited data seg size (kbytes, -d) unlimited scheduling priority (-e) 0 file size (blocks, -f) unlimited pending signals (-i) 8253291 max locked memory (kbytes, -l) 64 max memory size (kbytes, -m) unlimited open files (-n) 1048576 pipe size (512 bytes, -p) 8 POSIX message queues (bytes, -q) 819200 real-time priority (-r) 0 stack size (kbytes, -s) 8192 cpu time (seconds, -t) unlimited max user processes (-u) unlimited virtual memory (kbytes, -v) unlimited file locks (-x) unlimited ### 🐛 Describe the bug root@vllm-worker-6dd66f997f-pj6g4:~# ulimit -a real-time non-blocking time (microseconds, -R) unlimited core file size (blocks, -c) unlimited data seg size (kbytes, -d) unlimited scheduling priority (-e) 0 file size (blocks, -f) unlimited pending signals (-i) 8253291 max locked memory (kbytes, -l) 64 max memory size (kbytes, -m) unlimited open files (-n) https://github.com/vllm-project/vllm/commit/104857607ca8efe7c4a20160fc072c525e5ab7ad pipe size (512 bytes, -p) 8 POSIX message queues (bytes, -q) 819200 real-time prio...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: (-n) 1048576 pipe size (512 bytes, -p) 8 POSIX message queues (bytes, -q) 819200 real-time priority (-r) 0 stack size (kbytes, -s) 8192 cpu time (seconds, -t) unlimited max user processes (-u) unlim
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 02-16 02:29:16 api_server.py:838] vLLM API server version 0.7.1 INFO 02-16 02:29:16 api_server.py:839] args: Namespace(subparser='serve', model_tag='/vllm-workspace/deepseek-r1', config='', host=N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Use 3 node with 8*H100 to serve Deepseek R1 model, error is pthread_create failed: Resource temporarily unavailable bug ### Your current environment root@vllm-worker-6dd66f997f-pj6g4:~# **ulimit -a** real-time no...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Use 3 node with 8*H100 to serve Deepseek R1 model, error is pthread_create failed: Resource temporarily unavailable bug ### Your current environment root@vllm-worker-6dd66f997f-pj6g4:~# **ulimit -a** real-time no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
