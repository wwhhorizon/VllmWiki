# vllm-project/vllm#7141: [Bug]: Can't load Gemma2 model (9b-it, 27b-it)

| 字段 | 值 |
| --- | --- |
| Issue | [#7141](https://github.com/vllm-project/vllm/issues/7141) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't load Gemma2 model (9b-it, 27b-it)

### Issue 正文摘录

### Your current environment pip install vllm vllm version: 0.5.3post1 ### 🐛 Describe the bug ## Trigger model_params = { "model": 'google/gemma-2-9b-it', "quantization": "fp8", "dtype": "auto", "tensor_parallel_size": 1, "gpu_memory_utilization": 0.95, "max_model_len": 4096, "max_num_seqs": 256, "enable_prefix_caching": False, "enforce_eager": True, "seed": SEED, } llm = LLM(**model_params) ### Error `RuntimeError Traceback (most recent call last) Cell In[13], [line 14](vscode-notebook-cell:?execution_count=13&line=14) [1](vscode-notebook-cell:?execution_count=13&line=1) model_params = { [2](vscode-notebook-cell:?execution_count=13&line=2) "model": CFG.llm_model_id, [3](vscode-notebook-cell:?execution_count=13&line=3) "quantization": "fp8", (...) [11](vscode-notebook-cell:?execution_count=13&line=11) "seed": SEED, [12](vscode-notebook-cell:?execution_count=13&line=12) } ---> [14](vscode-notebook-cell:?execution_count=13&line=14) model_llm = CustomLLM(model_params) Cell In[12], [line 3](vscode-notebook-cell:?execution_count=12&line=3) [2](vscode-notebook-cell:?execution_count=12&line=2) def __init__(self, model_params): ----> [3](vscode-notebook-cell:?execution_count=12&line=3) se...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: g ## Trigger model_params = { "model": 'google/gemma-2-9b-it', "quantization": "fp8", "dtype": "auto", "tensor_parallel_size": 1, "gpu_memory_utilization": 0.95, "max_model_len": 4096, "max_num_seqs": 256, "enable_prefi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Can't load Gemma2 model (9b-it, 27b-it) bug ### Your current environment pip install vllm vllm version: 0.5.3post1 ### 🐛 Describe the bug ## Trigger model_params = { "model": 'google/gemma-2-9b-it', "quantization...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ing/.venv/lib/python3.10/site-packages/vllm/entrypoints/llm.py:157) self.request_counter = Counter() File ~/vllm-chunking/.venv/lib/python3.10/site-packages/vllm/engine/llm_engine.py:441, in LLMEngine.from_engine_args(c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: load Gemma2 model (9b-it, 27b-it) bug ### Your current environment pip install vllm vllm version: 0.5.3post1 ### 🐛 Describe the bug ## Trigger model_params = { "model": 'google/gemma-2-9b-it', "quantization": "fp8", "dt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .venv/lib/python3.10/site-packages/vllm/worker/model_runner.py:681) with CudaMemoryProfiler() as m: --> [682](https://vscode-remote+ssh-002dremote-002bgenai-002droot.vscode-resource.vscode-cdn.net/root/vllm-chunking/chu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
