# vllm-project/vllm#16718: [Bug]: Vllm serve‘s results is not equal to offline inference.

| 字段 | 值 |
| --- | --- |
| Issue | [#16718](https://github.com/vllm-project/vllm/issues/16718) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 40; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm serve‘s results is not equal to offline inference.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use the following function to start a vllm server. ``` def start_vllm_server( model_path: str, model_name: str, port: int = 8000, host: str = "0.0.0.0", gpu_memory_utilization: float = 0.9, max_model_len: int = 8192, dtype: str = "bfloat16", tensor_parallel_size: Optional[int] = None, pipeline_parallel_size: Optional[int] = None, generation_config: Optional[str] = None, ): """Start the vLLM server with the specified parameters.""" # Build the command cmd = [ "python", "-m", "vllm.entrypoints.openai.api_server", "--model", model_path, "--host", host, "--port", str(port), "--gpu-memory-utilization", str(gpu_memory_utilization), "--max-model-len", str(max_model_len), "--dtype", dtype, "--enforce-eager", "--served-model-name", model_name, ] # Add tensor parallel size if specified if tensor_parallel_size is not None: cmd.extend(["--tensor-parallel-size", str(tensor_parallel_size)]) # Add tensor parallel size if specified if pipeline_parallel_size is not None: cmd.extend(["--pipeline-parallel-size", str(pipeline_parallel_size)]) # Add generation config if specified if generation_config is not None: cmd.extend(["--generation-config",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onfig: Optional[str] = None, ): """Start the vLLM server with the specified parameters.""" # Build the command cmd = [ "python", "-m", "vllm.entrypoints.openai.api_server", "--model", model_path, "--host", host, "--port...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ollowing function to start a vllm server. ``` def start_vllm_server( model_path: str, model_name: str, port: int = 8000, host: str = "0.0.0.0", gpu_memory_utilization: float = 0.9, max_model_len: int = 8192, dtype: str...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: gpu_memory_utilization: float = 0.9, max_model_len: int = 8192, dtype: str = "bfloat16", tensor_parallel_size: Optional[int] = None, pipeline_parallel_size: Optional[int] = None, generation_config: Optional[str] = None,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: vLLM server: {e}") sys.exit(1) ``` And I also use an old code to evaluate my Qwen2-VL model: ``` # Qwen2-VL def init_qwen2_vl(model_name_or_path: str, gpu_memory_utilization: float, **kwargs): from vllm import LLM try:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
