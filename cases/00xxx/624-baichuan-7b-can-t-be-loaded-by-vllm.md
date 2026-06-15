# vllm-project/vllm#624: Baichuan-7B can't be loaded by vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#624](https://github.com/vllm-project/vllm/issues/624) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Baichuan-7B can't be loaded by vllm

### Issue 正文摘录

Hi, I'm a biginner to vllm. And I'm trying to use vllm to load Baichuan-7B, but meet this issue. ``` (venv) user@rtx4090x8:~/tonghu/vllm$ python -m vllm.entrypoints.api_server --model /huggingface.co/baichuan-inc/Baichuan-7B --host 0.0.0.0 --port 9000 INFO 07-31 15:39:30 llm_engine.py:60] Initializing an LLM engine with config: model='/huggingface.co/baichuan-inc/Baichuan-7B', tokenizer='/huggingface.co/baichuan-inc/Baichuan-7B', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/home/user/tonghu/vllm/venv/lib/python3.8/site-packages/vllm/entrypoints/api_server.py", line 78, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/user/tonghu/vllm/venv/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 232, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/home/user/tonghu/vllm/venv/lib/python3.8/site-packages/vllm/e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: v) user@rtx4090x8:~/tonghu/vllm$ python -m vllm.entrypoints.api_server --model /huggingface.co/baichuan-inc/Baichuan-7B --host 0.0.0.0 --port 9000 INFO 07-31 15:39:30 llm_engine.py:60] Initializing an LLM engine with co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: kenizer='/huggingface.co/baichuan-inc/Baichuan-7B', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: chuan-7B', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or: Tokenizer class BaiChuanTokenizer does not exist or is not currently imported. ``` I also tried it with llama2-7b-chat, it works well. ``` (venv) user@rtx4090x8:~/tonghu/vllm$ python -m vllm.entrypoints.api_server -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g to use vllm to load Baichuan-7B, but meet this issue. ``` (venv) user@rtx4090x8:~/tonghu/vllm$ python -m vllm.entrypoints.api_server --model /huggingface.co/baichuan-inc/Baichuan-7B --host 0.0.0.0 --port 9000 INFO 07-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
