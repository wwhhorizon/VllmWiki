# vllm-project/vllm#337: _pickle.UnpicklingError: could not find MARK when loading wizardcoder

| 字段 | 值 |
| --- | --- |
| Issue | [#337](https://github.com/vllm-project/vllm/issues/337) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> _pickle.UnpicklingError: could not find MARK when loading wizardcoder

### Issue 正文摘录

Thanks for fixing #254 . After I updated the code to the latest version, when I executed the following command: ``` python -m vllm.entrypoints.openai.api_server --model /home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/ ``` the following error occurred: ``` INFO 07-03 08:38:16 llm_engine.py:60] Initializing an LLM engine with config: model='/home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/', tokenizer='/home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/home/foo/anaconda3/envs/aigc/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/home/foo/anaconda3/envs/aigc/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/foo/workshop/vllm/vllm/entrypoints/openai/api_server.py", line 313, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/foo/workshop/vllm/vllm/engine/async_llm_engine.py", line 212, in from_engine_args eng...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: he following command: ``` python -m vllm.entrypoints.openai.api_server --model /home/foo/workshop/text-generation-webui/models/WizardLM_WizardCoder-15B-V1.0/ ``` the following error occurred: ``` INFO 07-03 08:38:16 llm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ation-webui/models/WizardLM_WizardCoder-15B-V1.0/', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oder bug Thanks for fixing #254 . After I updated the code to the latest version, when I executed the following command: ``` python -m vllm.entrypoints.openai.api_server --model /home/foo/workshop/text-generation-webui/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 5B-V1.0/', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/home/foo/anaconda3/envs/ai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: zardcoder bug Thanks for fixing #254 . After I updated the code to the latest version, when I executed the following command: ``` python -m vllm.entrypoints.openai.api_server --model /home/foo/workshop/text-generation-w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
