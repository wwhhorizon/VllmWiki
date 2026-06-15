# vllm-project/vllm#15336: [Bug]: Deploy DeepSeek R1 671B ,ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')")

| 字段 | 值 |
| --- | --- |
| Issue | [#15336](https://github.com/vllm-project/vllm/issues/15336) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploy DeepSeek R1 671B ,ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')")

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the following command, I encounter an error. ``` python3 -m vllm.entrypoints.openai.api_server \ --model=/data/deepseek-r1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.90 \ --max-num-seqs 128 \ --trust-remote-code \ --enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --port 8888 ``` The error is as follows: ``` INFO 03-22 06:48:13 [loader.py:429] Loading weights took 19.04 seconds ERROR 03-22 06:48:14 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution. ERROR 03-22 06:48:14 [worker_base.py:620] Traceback (most recent call last): ERROR 03-22 06:48:14 [worker_base.py:620] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 612, in execute_ method ERROR 03-22 06:48:14 [worker_base.py:620] return run_method(self, method, args, kwargs) ERROR 03-22 06:48:14 [worker_base.py:620] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-22 06:48:14 [worker_base.py:620...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Deploy DeepSeek R1 671B ,ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')") bug ### Your current environment ### 🐛 Describe the bug When I run the fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 623, in run ERROR 03-22 06:48:14 [worker_base.py:620] kernel = self.compile( ERROR 03-22 06:48:14 [worker_base.py:620] ^^^^^^^^^^^^^ ERROR 03-22 06:48:14 [worker_base.py:620] File "/usr/local/lib/python3.12/dist-package...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: r \ --model=/data/deepseek-r1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --gpu-memory-utili...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Deploy DeepSeek R1 671B ,ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')") bug ### Your current environment ### 🐛 Describe the bug When I run the following...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: remote-code \ --enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --port 8888 ``` The error is as follows: ``` INFO 03-22 06:48:13 [loader.py:429] Loading weights took 19.04 seconds E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
