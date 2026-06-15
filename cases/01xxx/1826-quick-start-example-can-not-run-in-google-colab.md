# vllm-project/vllm#1826: `quick start` example can not run in google colab

| 字段 | 值 |
| --- | --- |
| Issue | [#1826](https://github.com/vllm-project/vllm/issues/1826) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> `quick start` example can not run in google colab

### Issue 正文摘录

## question Can vllm run in google colab? ## infomation I tried `V100 GPU` and `A100 GPU` ``` > ! python --version Python 3.10.12 > !nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:33:58_PDT_2022 Cuda compilation tools, release 11.8, V11.8.89 Build cuda_11.8.r11.8/compiler.31833905_0 ``` ## steps I followed these two tutorial in google colab: `https://docs.vllm.ai/en/latest/getting_started/installation.html` follow `cuda 11.8` section (default install vllm can not run neither): ``` # Install vLLM with CUDA 11.8. # Replace `cp310` with your Python version (e.g., `cp38`, `cp39`, `cp311`). !pip install https://github.com/vllm-project/vllm/releases/download/v0.2.2/vllm-0.2.2+cu118-cp310-cp310-manylinux1_x86_64.whl # Re-install PyTorch with CUDA 11.8. !pip uninstall torch -y !pip install torch --upgrade --index-url https://download.pytorch.org/whl/cu118 ``` follow `https://docs.vllm.ai/en/latest/getting_started/quickstart.html` ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = Sampl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: colab? ## infomation I tried `V100 GPU` and `A100 GPU` ``` > ! python --version Python 3.10.12 > !nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:33...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) -------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: tion Can vllm run in google colab? ## infomation I tried `V100 GPU` and `A100 GPU` ``` > ! python --version Python 3.10.12 > !nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ") 29 frames [/usr/local/lib/python3.10/dist-packages/xformers/ops/fmha/dispatch.py](https://localhost:8080/#) in _run_priority_list(name, priority_list, inp) 61 return op 62 not_supported_reasons.append(not_supported)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") ``` and get error: ``` INFO 11-29 06:07:20 llm_engine.py:72] Initializing an LLM engine with config: model='facebook/opt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
