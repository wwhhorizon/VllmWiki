# vllm-project/vllm#16918: Qwen2.5 VL and gemma-3-12b error on  VLLM 8.4

| 字段 | 值 |
| --- | --- |
| Issue | [#16918](https://github.com/vllm-project/vllm/issues/16918) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | cuda;gemm |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen2.5 VL and gemma-3-12b error on  VLLM 8.4

### Issue 正文摘录

### Your current environment cuda：12.1 1. 启动脚本(command) vllm serve Qwen2.5-VL-3B-Instruct --tensor-parallel-size 1 --max-model-len 12800 --max-num-batched-tokens 12800 --port 10880 --trust-remote-code --served-model-name qwen2.5_3B --limit-mm-per-prompt image=2 2. 请求参数 `{ "model": "qwen2.5_3B", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "请描述这张图片" }, { "type": "image_url", "image_url": { "url": "http://pic5.40017.cn/i/ori/1urNSLvgq8o.jpg" } } ] } ] }` 3、报错信息 ERROR 04-21 18:26:31 [serving_chat.py:200] Error in preprocessing prompt inputs ERROR 04-21 18:26:31 [serving_chat.py:200] Traceback (most recent call last): ERROR 04-21 18:26:31 [serving_chat.py:200] File "/opt/conda/envs/vllm8/lib/python3.10/site-packages/vllm/entrypoints/openai/serving_chat.py", line 183, in create_chat_completion ERROR 04-21 18:26:31 [serving_chat.py:200] ) = await self._preprocess_chat( ERROR 04-21 18:26:31 [serving_chat.py:200] File "/opt/conda/envs/vllm8/lib/python3.10/site-packages/vllm/entrypoints/openai/serving_engine.py", line 422, in _preprocess_chat ERROR 04-21 18:26:31 [serving_chat.py:200] mm_data = await mm_data_future ERROR 04-21 18:26:31 [serving_chat.py:200] File "...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Qwen2.5 VL and gemma-3-12b error on VLLM 8.4 usage;stale ### Your current environment cuda：12.1 1. 启动脚本(command) vllm serve Qwen2.5-VL-3B-Instruct --tensor-parallel-size 1 --max-model-len 12800 --max-num-batched-token
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: in ERROR 04-21 18:26:31 [serving_chat.py:200] modality: await asyncio.gather(*items) ERROR 04-21 18:26:31 [serving_chat.py:200] File "/opt/conda/envs/vllm8/lib/python3.10/site-packages/vllm/multimodal/utils.py", line 20...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Qwen2.5 VL and gemma-3-12b error on VLLM 8.4 usage;stale ### Your current environment cuda：12.1 1. 启动脚本(command) vllm serve Qwen2.5-VL-3B-Instruct --tensor-parallel-size 1 --max-model-len 12800 --max-num-batched-tokens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gemma-3-12b error on VLLM 8.4 usage;stale ### Your current environment cuda：12.1 1. 启动脚本(command) vllm serve Qwen2.5-VL-3B-Instruct --tensor-parallel-size 1 --max-model-len 12800 --max-num-batched-tokens 12800 --port 10...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: break f.write(chunk) else: print(f"Failed to retrieve image. Status code: {response.status}") if __name__ == '__main__': image_url = 'http://pic5.40017.cn/i/ori/1urNSLvgq8o.jpg' file_path = 'downloaded_image.jpg'

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
