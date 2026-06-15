# vllm-project/vllm#9152: [Bug]: Can not pip install vllm inside docker

| 字段 | 值 |
| --- | --- |
| Issue | [#9152](https://github.com/vllm-project/vllm/issues/9152) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can not pip install vllm inside docker

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what inside my Dockerfile ```dockerfile FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-devel AS build RUN apt update && apt install gcc g++ git -y && apt clean && rm -rf /var/lib/apt/lists/* ENV PATH=/workspace-lib:/workspace-lib/bin:$PATH ENV PYTHONUSERBASE=/workspace-lib RUN git clone https://github.com/vllm-project/vllm.git /root/vllm RUN pip install git+https://github.com/vllm-project/vllm.git --no-cache-dir --user FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime AS vllm-openai WORKDIR /vllm-workspace COPY --from=build /workspace-lib /workspace-lib ENV PATH=/workspace-lib:/workspace-lib/bin:$PATH ENV PYTHONUSERBASE=/workspace-lib ENV PYTHONPATH=/workspace-lib:/vllm-workspace ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server"] ``` And here is how I build it ```bash docker build . -t fahadh4ilyas/gpt-svc-vllm --target vllm-openai --no-cache ``` But, I got this error ```bash 1130.5 ptxas /tmp/tmpxft_0000040d_00000000-11_attention_kernels.compute_50.ptx, line 5016842; error : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher 1130.5 ptxas /t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Can not pip install vllm inside docker bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what inside my Dockerfile ```dockerfile FROM pytorch/pytorch:2.4.0-cuda12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e is what inside my Dockerfile ```dockerfile FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-devel AS build RUN apt update && apt install gcc g++ git -y && apt clean && rm -rf /var/lib/apt/lists/* ENV PATH=/workspace-lib:/wo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _in_process.py", line 251, in build_wheel 1130.5 return _build_backend().build_wheel(wheel_directory, config_settings, 1130.5 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 1130.5 File "/tmp/pip-build-en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pip install vllm inside docker bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what inside my Dockerfile ```dockerfile FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-devel...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ted due to errors 1130.5 [21/130] Building CUDA object CMakeFiles/_moe_C.dir/csrc/moe/marlin_kernels/marlin_moe_kernel_ku4.cu.o 1130.5 [22/130] Building CUDA object CMakeFiles/_moe_C.dir/csrc/moe/marlin_kernels/marlin_m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
