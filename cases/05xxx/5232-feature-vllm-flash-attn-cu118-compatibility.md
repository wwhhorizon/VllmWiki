# vllm-project/vllm#5232: [Feature]: vllm-flash-attn cu118 compatibility 

| 字段 | 值 |
| --- | --- |
| Issue | [#5232](https://github.com/vllm-project/vllm/issues/5232) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm-flash-attn cu118 compatibility 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vllm-flash-attn seems like it currently does not support cu118: ``` >>> import vllm_flash_attn Traceback (most recent call last): File " ", line 1, in File "/opt/pyenv/versions/3.10.9/lib/python3.10/site-packages/vllm_flash_attn/__init__.py", line 3, in from vllm_flash_attn.flash_attn_interface import ( File "/opt/pyenv/versions/3.10.9/lib/python3.10/site-packages/vllm_flash_attn/flash_attn_interface.py", line 10, in import vllm_flash_attn_2_cuda as flash_attn_cuda ImportError: libcudart.so.12: cannot open shared object file: No such file or directory ``` flash-attn seems to support cu118 on the original project and vllm supports cu118 so vllm-flash-attn cu118 version would be helpful ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vllm-flash-attn seems like it currently does not support cu118: ``` >>> import vllm_flash_attn Traceback (most recent call last): File " ", line 1, in File "/opt/pyenv/versions/3.10.9/lib/python3.10/site-packages/vllm_f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: vllm-flash-attn cu118 compatibility feature request;stale ### 🚀 The feature, motivation and pitch vllm-flash-attn seems like it currently does not support cu118: ``` >>> import vllm_flash_attn Traceback (most...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ttn/flash_attn_interface.py", line 10, in import vllm_flash_attn_2_cuda as flash_attn_cuda ImportError: libcudart.so.12: cannot open shared object file: No such file or directory ``` flash-attn seems to support cu118 on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
