# vllm-project/vllm#32730: [Bug]: CPU tests hit CUDA path when VLLM_TARGET_DEVICE=cpu [CPU Backend]

| 字段 | 值 |
| --- | --- |
| Issue | [#32730](https://github.com/vllm-project/vllm/issues/32730) |
| 状态 | open |
| 标签 | bug;stale;cpu |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU tests hit CUDA path when VLLM_TARGET_DEVICE=cpu [CPU Backend]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM tests on a CPU-only machine with `VLLM_TARGET_DEVICE=cpu`, the basic correctness and engine tests still select GPU-only paths (e.g., `FLASH_ATTN` and `gpu_model_runner`), which then crash with: ``` AssertionError: Torch not compiled with CUDA enabled File ".../vllm/v1/worker/gpu_model_runner.py", line 210, in __init__ default_stream = torch.cuda.current_stream() ``` This makes CPU test execution effectively impossible even when explicitly targeting CPU. ### Reproduction On a Linux machine without GPU (or with CPU-only PyTorch): ```bash # Clone vLLM and checkout v0.13.0 git clone https://github.com/vllm-project/vllm.git && cd vllm git checkout v0.13.0 # Install CPU-only PyTorch pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu # Install build dependencies pip install -r requirements/cpu.txt pip install -r requirements/cpu-build.txt # Build and install vLLM for CPU VLLM_TARGET_DEVICE=cpu pip install -e . # Verify the build (version should contain "+cpu") python -c "import vllm; print(vllm.__version__)" # Expected output: something like 0.x.x+cpu # Run tests (these will fail...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: pu_model_runner`), which then crash with: ``` AssertionError: Torch not compiled with CUDA enabled File ".../vllm/v1/worker/gpu_model_runner.py", line 210, in __init__ default_stream = torch.cuda.current_stream() ``` Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CPU tests hit CUDA path when VLLM_TARGET_DEVICE=cpu [CPU Backend] bug;stale;cpu ### Your current environment ### 🐛 Describe the bug When running vLLM tests on a CPU-only machine with `VLLM_TARGET_DEVICE=cpu`, the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: CPU tests hit CUDA path when VLLM_TARGET_DEVICE=cpu [CPU Backend] bug;stale;cpu ### Your current environment ### 🐛 Describe the bug When running vLLM tests on a CPU-only machine with `VLLM_TARGET_DEVICE=cpu`, the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nd engine tests still select GPU-only paths (e.g., `FLASH_ATTN` and `gpu_model_runner`), which then crash with: ``` AssertionError: Torch not compiled with CUDA enabled File ".../vllm/v1/worker/gpu_model_runner.py", lin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: CPU tests hit CUDA path when VLLM_TARGET_DEVICE=cpu [CPU Backend] bug;stale;cpu ### Your current environment ### 🐛 Describe the bug When running vLLM tests on a CPU-only machine with `VLLM_TARGET_DEVICE=cpu`, the bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
