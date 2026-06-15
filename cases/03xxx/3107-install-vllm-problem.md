# vllm-project/vllm#3107: install vllm problem:

| 字段 | 值 |
| --- | --- |
| Issue | [#3107](https://github.com/vllm-project/vllm/issues/3107) |
| 状态 | closed |
| 标签 | unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> install vllm problem:

### Issue 正文摘录

## dependency probelm install `vllm==0.3.2+cu118` through `pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl` with ``` export VLLM_VERSION=0.3.2 export PYTHON_VERSION=311 ``` BUT, the vllm whl depend on `cupy_cuda12x` ... ## detail install log ``` ❯ pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl Collecting vllm==0.3.2+cu118 Downloading https://github.com/vllm-project/vllm/releases/download/v0.3.2/vllm-0.3.2+cu118-cp311-cp311-manylinux1_x86_64.whl (41.2 MB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.2/41.2 MB 2.5 MB/s eta 0:00:00 Collecting ninja (from vllm==0.3.2+cu118) Using cached ninja-1.11.1.1-py2.py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (5.3 kB) Requirement already satisfied: psutil in /opt/conda/envs/envd/lib/python3.11/site-packages (from vllm==0.3.2+cu118) (5.9.8) Collecting ray>=2.9 (from vllm==0.3.2+cu118) Using cached ray-2.9.3-cp311-cp311-manylinux2014_x86_64.whl.metadata (13 kB) Collecting sentencepiece...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: install vllm problem: unstale ## dependency probelm install `vllm==0.3.2+cu118` through `pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .11/site-packages (from ray>=2.9->vllm==0.3.2+cu118) (2.28.1) Collecting huggingface-hub =0.19.3 (from transformers>=4.38.0->vllm==0.3.2+cu118) Using cached huggingface_hub-0.21.3-py3-none-any.whl.metadata (13 kB) Colle...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: install vllm problem: unstale ## dependency probelm install `vllm==0.3.2+cu118` through `pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 11.5.0-py3-none-any.whl.metadata (7.8 kB) Requirement already satisfied: triton>=2.1.0 in /opt/conda/envs/envd/lib/python3.11/site-packages (from vllm==0.3.2+cu118) (2.1.0) Collecting cupy-cuda12x==12.1.0 (from vllm==0....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (49 kB) Collecting quantile-python>=1.1 (from aioprometheus[starlette]->vllm==0.3.2+cu118) Using cached quantile-python-1.1.tar.gz (2.9 kB) Preparing metadata (setup...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
