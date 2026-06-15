# vllm-project/vllm#27812: [Bug]:  subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=15', '--target=_moe_C', '--target=_vllm_fa2_C', '--target=_vllm_fa3_C', '--target=_flashmla_C', '--target=cumem_allocator', '--target=_C']' returned non-zero exit status 137.

| 字段 | 值 |
| --- | --- |
| Issue | [#27812](https://github.com/vllm-project/vllm/issues/27812) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=15', '--target=_moe_C', '--target=_vllm_fa2_C', '--target=_vllm_fa3_C', '--target=_flashmla_C', '--target=cumem_allocator', '--target=_C']' returned non-zero exit status 137.

### Issue 正文摘录

### Your current environment I'm not sure collect_env script is relevant here since I'm using docker for isolation of my env and the dockerfiles I'm using and for which I'm reporting the error are https://github.com/ModelTC/LightX2V/blob/main/Dockerfile and https://github.com/ModelTC/LightX2V/blob/main/Dockerfile_cu124 I'm running docker on ubuntu with: ``` | NVIDIA-SMI 550.127.08 Driver Version: 550.127.08 CUDA Version: 12.4 | ``` ### 🐛 Describe the bug The install command I'm running in the docker and fails (see Docker file) is : ``` RUN git clone https://github.com/vllm-project/vllm.git -b v0.10.0 && cd vllm \ && python use_existing_torch.py && pip install -r requirements/build.txt \ && pip install --no-cache-dir --no-build-isolation -v -e . ``` Failed to build [Dockerfile_cu124 ](https://github.com/ModelTC/LightX2V/blob/main/Dockerfile_cu124) ``` 3039.4 File " ", line 268, in run 3039.4 File "/opt/conda/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 99, in run 3039.4 _build_ext.run(self) 3039.4 File "/opt/conda/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run 3039.4 self.build_extensions() 3039.4 File " ", line 242...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=15', '--target=_moe_C', '--target=_vllm_fa2_C', '--target=_vllm_fa3_C', '--target=_flashmla_C', '--target=cumem_allocator', '--target=_C']' re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: in/Dockerfile_cu124 I'm running docker on ubuntu with: ``` | NVIDIA-SMI 550.127.08 Driver Version: 550.127.08 CUDA Version: 12.4 | ``` ### 🐛 Describe the bug The install command I'm running in the docker and fails (see...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: '.', '-j=15', '--target=_moe_C', '--target=_vllm_fa2_C', '--target=_vllm_fa3_C', '--target=_flashmla_C', '--target=cumem_allocator', '--target=_C']' returned non-zero exit status 137. bug ### Your current environment I'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s I'm using and for which I'm reporting the error are https://github.com/ModelTC/LightX2V/blob/main/Dockerfile and https://github.com/ModelTC/LightX2V/blob/main/Dockerfile_cu124 I'm running docker on ubuntu with: ``` |...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: lledProcessError: Command '['cmake', '--build', '.', '-j=15', '--target=_moe_C', '--target=_vllm_fa2_C', '--target=_vllm_fa3_C', '--target=_flashmla_C', '--target=cumem_allocator', '--target=_C']' returned non-zero exit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
