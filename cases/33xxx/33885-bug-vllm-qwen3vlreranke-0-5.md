# vllm-project/vllm#33885: [Bug]: 用vllm启动Qwen3VLReranke接口在重排任何图像时获取的得分很低仅有0.5左右

| 字段 | 值 |
| --- | --- |
| Issue | [#33885](https://github.com/vllm-project/vllm/issues/33885) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 用vllm启动Qwen3VLReranke接口在重排任何图像时获取的得分很低仅有0.5左右

### Issue 正文摘录

### Your current environment docker run --gpus '"device=7"' --entrypoint "" -v /dataset/models/Qwen/Qwen3-VL-Reranker-8B:/model -p 9091:8000 --shm-size=8g vllm/vllm-openai:v0.15.1-cu130 vllm serve /model --runner pooling --max-model-len 16384 --gpu-memory-utilization 0.5 --dtype bfloat16 --hf-overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --chat-template /model/qwen3_vl_reranker.jinja --trust-remote-code ### 🐛 Describe the bug 用千问官方的重排列子获取的结果如下Document 1 (文本): 0.8508 Document 2 (图片): 0.5273 Document 3 (文本 + 图片): 0.7789 也是差别很大。。对于图片来说目前通过接口获取得分有bug ```python3 import argparse import pprint import requests # ===== 配置 ===== QUERY = "A woman playing with her dog on a beach at sunset." TEXT_DOC = ( "A woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset, " "as the dog offers its paw in a heartwarming display of companionship and trust." ) IMAGE_URL = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg" # 获取模型名称（可选） def get_model_name(base_url: str) -> str: try: resp = requests.get(f"{base_url}/v1/models") resp.raise_for_status() return...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: pooling --max-model-len 16384 --gpu-memory-utilization 0.5 --dtype bfloat16 --hf-overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": tru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 用vllm启动Qwen3VLReranke接口在重排任何图像时获取的得分很低仅有0.5左右 bug ### Your current environment docker run --gpus '"device=7"' --entrypoint "" -v /dataset/models/Qwen/Qwen3-VL-Reranker-8B:/model -p 9091:8000 --shm-size=8g vllm/vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Qwen3VLReranke接口在重排任何图像时获取的得分很低仅有0.5左右 bug ### Your current environment docker run --gpus '"device=7"' --entrypoint "" -v /dataset/models/Qwen/Qwen3-VL-Reranker-8B:/model -p 9091:8000 --shm-size=8g vllm/vllm-openai:v0.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --gpu-memory-utilization 0.5 --dtype bfloat16 --hf-overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --chat-template /model/qwe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: code == 200: pprint.pprint(response.json()) else: print("❌ Response body:") print(response.text) except Exception as e: print(f"💥 Request failed: {e}") print("-" * 60) if __name__ == "__main__": pars

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
