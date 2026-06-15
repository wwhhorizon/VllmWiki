# vllm-project/vllm#254: AssertionError when load WizardLM_WizardCoder-15B-V1.0

| 字段 | 值 |
| --- | --- |
| Issue | [#254](https://github.com/vllm-project/vllm/issues/254) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError when load WizardLM_WizardCoder-15B-V1.0

### Issue 正文摘录

I pulled the latest code and ran `pip install . -e`, and then got the following error when executing `python -m vllm.entrypoints.api_server --model /home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/` command: ``` INFO 06-26 04:42:39 llm_engine.py:59] Initializing an LLM engine with config: model='/home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/home/foo/anaconda3/envs/aigc/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/home/foo/anaconda3/envs/aigc/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/foo/workshop/vllm/vllm/entrypoints/api_server.py", line 82, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/foo/workshop/vllm/vllm/engine/async_llm_engine.py", line 212, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/home/foo/workshop/vllm/vllm/engine/async_llm_engine.py", line 49, in __init__ self.engine = engine_class(*args, **kwargs)...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: o/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: following error when executing `python -m vllm.entrypoints.api_server --model /home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/` command: ``` INFO 06-26 04:42:39 llm_engine.py:59] Initializi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: WizardLM_WizardCoder-15B-V1.0 bug I pulled the latest code and ran `pip install . -e`, and then got the following error when executing `python -m vllm.entrypoints.api_server --model /home/foo/workshop/text-generation-we...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: izardLM_WizardCoder-15B-V1.0/', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/home/foo/anaconda3/envs/ai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ssertionError when load WizardLM_WizardCoder-15B-V1.0 bug I pulled the latest code and ran `pip install . -e`, and then got the following error when executing `python -m vllm.entrypoints.api_server --model /home/foo/wor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
