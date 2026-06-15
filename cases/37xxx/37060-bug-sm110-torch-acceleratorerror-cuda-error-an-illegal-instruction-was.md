# vllm-project/vllm#37060: [Bug]: sm110: torch.AcceleratorError: CUDA error: an illegal instruction was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#37060](https://github.com/vllm-project/vllm/issues/37060) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sm110: torch.AcceleratorError: CUDA error: an illegal instruction was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, Unfortunately I failed to tun NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 on the Nvidia Jetson Thor. See below logs. Commands to reproduce: ``` # 1. Create a fresh venv uv venv .vllm --python 3.12 source .vllm/bin/activate # 2. Install PyTorch with CUDA 13 uv pip install torch torchvision torchaudio \ --index-url https://download.pytorch.org/whl/cu130 # 3. Set environment for SM 110 export TORCH_CUDA_ARCH_LIST=11.0a export CUDA_HOME=/usr/local/cuda-13 export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas export PATH="${CUDA_HOME}/bin:$PATH" # 4. Build vLLM from source git clone https://github.com/vllm-project/vllm.git cd vllm python3 use_existing_torch.py uv pip install -r requirements/build.txt MAX_JOBS=$(nproc) python3 setup.py bdist_wheel uv pip install -r requirements/common.txt uv pip install --no-deps dist/vllm*.whl cd .. # 5. Build FlashInfer from source git clone --recursive https://github.com/flashinfer-ai/flashinfer.git cd flashinfer export FLASHINFER_CUDA_ARCH_LIST="11.0a" uv pip install -r requirements.txt MAX_JOBS=$(nproc) python -m flashinfer.aot python3 -m build --no-isolation --wheel uv pip install --no-deps dist/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: max-cudagraph-capture-size 32 \ --max-num-seqs 32 \ --enable-chunked-prefill \ --host 0.0.0.0 \ --port 5000 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser-plugin "./super_v3_reasoning_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: a fresh venv uv venv .vllm --python 3.12 source .vllm/bin/activate # 2. Install PyTorch with CUDA 13 uv pip install torch torchvision torchaudio \ --index-url https://download.pytorch.org/whl/cu130 # 3. Set environment...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: Hello, Unfortunately I failed to tun NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 on the Nvidia Jetson Thor. See below logs. Commands to reproduce: ``` # 1. Create a fresh venv uv venv .vllm --python 3.12 source .vllm/bin/ac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: sm110: torch.AcceleratorError: CUDA error: an illegal instruction was encountered bug ### Your current environment ### 🐛 Describe the bug Hello, Unfortunately I failed to tun NVIDIA-Nemotron-3-Super-120B-A12B-NVFP
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rt TORCH_CUDA_ARCH_LIST=11.0a export CUDA_HOME=/usr/local/cuda-13 export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas export PATH="${CUDA_HOME}/bin:$PATH" # 4. Build vLLM from source git clone https://github.com/vllm-pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
