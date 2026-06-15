# vllm-project/vllm#8331: [Usage]: example/offline_inference_chat.py run error. 

| 字段 | 值 |
| --- | --- |
| Issue | [#8331](https://github.com/vllm-project/vllm/issues/8331) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: example/offline_inference_chat.py run error. 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a llama3. I don't know how to integrate it with vllm. I am a new user of vllm and a freshman in this domain. I want to use vllm v0.6.0 to run llama3 and do some research. When I run example/offline_inference_chat.py[https://github.com/vllm-project/vllm/blob/v0.6.0/examples/offline_inference_chat.py] which using llama3 model, I get error as below. I searched the related issue https://github.com/vllm-project/vllm/issues/4180 . after read it I am still not clear how to solve this problem. I also sign up in the HuggingFace. But how can I use the account in vllm? Coule someone please giive me some advice? I am a freshman in this domain and really don't know how to do next. Thank you advance! python examples/offline_inference_chat.py Traceback (most recent call last): File "/root/anaconda3/envs/vllmsourcebuildpython3.10/lib/python3.10/site-packages/huggingface_hub/utils/_errors.py", line 304, in hf_raise_for_status response.raise_for_status() File "/root/anaconda3/envs/vllmsourcebuildpython3.10/lib/python3.10/site-packages/requests/models.py", line...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: y` ``` ### How would you like to use vllm I want to run inference of a llama3. I don't know how to integrate it with vllm. I am a new user of vllm and a freshman in this domain. I want to use vllm v0.6.0 to run llama3 a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: example/offline_inference_chat.py run error. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a llama3. I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: raceback (most recent call last): File "/root/anaconda3/envs/vllmsourcebuildpython3.10/lib/python3.10/site-packages/huggingface_hub/utils/_errors.py", line 304, in hf_raise_for_status response.raise_for_status() File "/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in this domain. I want to use vllm v0.6.0 to run llama3 and do some research. When I run example/offline_inference_chat.py[https://github.com/vllm-project/vllm/blob/v0.6.0/examples/offline_inference_chat.py] which using...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 3.10/site-packages/huggingface_hub/file_download.py", line 1751, in _get_metadata_or_catch_e rror metadata = get_hf_file_metadata( File "/root/anaconda3/envs/vllmsourcebuildpython3.10/lib/python3.10/site-packages/huggin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
