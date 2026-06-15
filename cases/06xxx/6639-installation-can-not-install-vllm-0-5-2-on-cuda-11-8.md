# vllm-project/vllm#6639: [Installation]: Can not install vllm-0.5.2 on cuda-11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#6639](https://github.com/vllm-project/vllm/issues/6639) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Can not install vllm-0.5.2 on cuda-11.8

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` N/A. ### How you are installing vllm We installed vllm using docker as followings: ```sh RUN yum install -y tmux RUN pip install -U torch==2.3.1 torchvision==0.18.1 --index-url https://download.pytorch.org/whl/cu118 RUN pip install xformers==0.0.27 --index-url https://download.pytorch.org/whl/cu118 # for vllm-common [https://github.com/vllm-project/vllm/blob/v0.5.2/requirements-common.txt] RUN pip install cmake>=3.21 ninja psutil sentencepiece # numpy =4.42.4 tokenizers>=0.19.1 fastapi aiohttp openai uvicorn[standard] pydantic>=2.0 pillow prometheus_client>=0.18.0 prometheus-fastapi-instrumentator>=7.0.0 tiktoken>=0.6.0 lm-format-enforcer==0.10.3 # pip install outlines>=0.0.43, =3.10.4 pyzmq # for vllm-cuda [https://github.com/vllm-project/vllm/blob/v0.5.2/requirements-cuda.txt] RUN pip install ray>=2.9 nvidia-ml-py # torch == 2.3.1 # These must be updated alongside torch # torchvision == 0.18.1 # Required for phi3v processor. See https://github.com/pytorch/vision?tab=readme-ov-file#installation for corresponding version # xformers == 0.0.27 # Requires PyTorch 2.3.1 # vllm-flash-attn == 2.5.9.post1 # Re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Can not install vllm-0.5.2 on cuda-11.8 installation ### Your current environment ```text The output of `python collect_env.py` ``` N/A. ### How you are installing vllm We installed vllm using docker as
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ient>=0.18.0 prometheus-fastapi-instrumentator>=7.0.0 tiktoken>=0.6.0 lm-format-enforcer==0.10.3 # pip install outlines>=0.0.43, =3.10.4 pyzmq # for vllm-cuda [https://github.com/vllm-project/vllm/blob/v0.5.2/requiremen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: velopment attention_kv_cache;ci_build;distributed_parallel;model_support;quantization attention;cuda;quantization build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: Can not install vllm-0.5.2 on cuda-11.8 installation ### Your current environment ```text The output of `python collect_env.py` ``` N/A. ### How you are installing vllm We installed vllm using docker as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
