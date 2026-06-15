# vllm-project/vllm#2053: RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

| 字段 | 值 |
| --- | --- |
| Issue | [#2053](https://github.com/vllm-project/vllm/issues/2053) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

### Issue 正文摘录

Hi, thanks for this impressive project. I use vllm, which works well for llama quantized by awq. However, when I changed to falcon-40b (awq), it did not work. The version is the newest, and I serve this model online. I tried to use the hf transformer to generate a response, which performed normally without any error. ``` 2023-12-12 19:38:39 | ERROR | stderr | Traceback (most recent call last): 2023-12-12 19:38:39 | ERROR | stderr | File "/root/miniconda3/envs/fastchat/lib/python3.9/runpy.py", line 197, in _run_module_as_main 2023-12-12 19:38:39 | ERROR | stderr | return _run_code(code, main_globals, None, 2023-12-12 19:38:39 | ERROR | stderr | File "/root/miniconda3/envs/fastchat/lib/python3.9/runpy.py", line 87, in _run_code 2023-12-12 19:38:39 | ERROR | stderr | exec(code, run_globals) 2023-12-12 19:38:39 | ERROR | stderr | File "/root/miniconda3/envs/fastchat/lib/python3.9/site-packages/fastchat/serve/vllm_worker.py", line 243, in 2023-12-12 19:38:39 | ERROR | stderr | engine = AsyncLLMEngine.from_engine_args(engine_args) 2023-12-12 19:38:39 | ERROR | stderr | File "/root/miniconda3/envs/fastchat/lib/python3.9/site-packages/vllm/engine/async_llm_engine.py", line 495, in from_en...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Hi, thanks for this impressive project. I use vllm, which works well for llama quantized by awq. However, when I changed to falcon-40b (awq), it did not work. The version is the newest, and I serve this model online. I...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: line 208, in _init_cache 2023-12-12 19:38:39 | ERROR | stderr | num_blocks = self._run_workers( 2023-12-12 19:38:39 | ERROR | stderr | File "/root/miniconda3/envs/fastchat/lib/python3.9/site-packages/vllm/engine/llm_eng...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: awq. However, when I changed to falcon-40b (awq), it did not work. The version is the newest, and I serve this model online. I tried to use the hf transformer to generate a response, which performed normally without any...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: anks for this impressive project. I use vllm, which works well for llama quantized by awq. However, when I changed to falcon-40b (awq), it did not work. The version is the newest, and I serve this model online. I tried...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: fastchat/lib/python3.9/site-packages/vllm/worker/worker.py", line 88, in profile_num_available_blocks 2023-12-12 19:38:39 | ERROR | stderr | self.model_runner.profile_run() 2023-12-12 19:38:39 | ERROR | stderr | File "/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
