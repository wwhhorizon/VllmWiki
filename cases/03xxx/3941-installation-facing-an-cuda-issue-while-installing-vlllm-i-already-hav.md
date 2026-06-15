# vllm-project/vllm#3941: [Installation]: Facing an Cuda issue while installing vlllm. I already have CUDA toolkit installed.         device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),       No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1'       Traceback (most recent call last):

| 字段 | 值 |
| --- | --- |
| Issue | [#3941](https://github.com/vllm-project/vllm/issues/3941) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Facing an Cuda issue while installing vlllm. I already have CUDA toolkit installed.         device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),       No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1'       Traceback (most recent call last):

### Issue 正文摘录

### Your current environment StatusCode : 200 StatusDescription : OK Content : # ruff: noqa # code borrowed from https://github.com/pytorch/pytorch/blob/main/torch/utils/collect_env.py # Unlike the rest of the PyTorch this file must be python2 compliant. # This script outputs r... RawContent : HTTP/1.1 200 OK Connection: keep-alive Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; sandbox Strict-Transport-Security: max-age=31536000 X-Content-Type-Options: nosniff ... Forms : {} Headers : {[Connection, keep-alive], [Content-Security-Policy, default-src 'none'; style-src 'unsafe-inline'; sandbox], [Strict-Transport-Security, max-age=31536000], [X-Content-Type-Options, nosniff]...} Images : {} InputFields : {} Links : {} ParsedHtml : System.__ComObject RawContentLength : 24853 ### How you are installing vllm pip install vllm

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Facing an Cuda issue while installing vlllm. I already have CUDA toolkit installed. device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), No CUDA runtim
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: Facing an Cuda issue while installing vlllm. I already have CUDA toolkit installed. device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), No CUDA runtime is found, u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
