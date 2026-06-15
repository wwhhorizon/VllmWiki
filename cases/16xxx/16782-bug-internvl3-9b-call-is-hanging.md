# vllm-project/vllm#16782: [Bug]: InternVL3-9B call is hanging

| 字段 | 值 |
| --- | --- |
| Issue | [#16782](https://github.com/vllm-project/vllm/issues/16782) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL3-9B call is hanging

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --served-model-name InternVL3-9B --model /models/OpenGVLab/InternVL3-9B --trust-remote-code from openai import OpenAI client = OpenAI( api_key='EMPTY', base_url=f'http://127.0.0.1:8000/v1', ) model = client.models.list().data[0].id if __name__ == "__main__": print(f"all models:{client.models.list()}") print(f'model: {model}') messages = [{'role': 'user', 'content': [ {'type': 'image_url', 'image_url': {'url': 'http://img.ecej.com/dp/993276edbfbbeb262d9e053ded59f779.jpg'}}, {'type': 'text', 'text': '#角色：你是一个燃气设施与燃气燃烧器具、电器安全间距检测专家，需要判断间距是否存在隐患\n#图片清晰要求：\n1、图片清晰，可准确识别图片中各个元素\n2、图片中能够正常识别出燃气设施\n#间距要求：\n##电气设备与燃气管道的净距要求：\n1、明装的绝缘电线或电缆：\n平行敷设：250毫米\n交叉敷设：100毫米\n2、暗装或管内绝缘电线：\n平行敷设：50毫米（从所作的槽或管的边缘算起）\n交叉敷设：10毫米\n3、电压小于1000V的裸露电线的导电部分：\n平行敷设：1000毫米（潮湿地区推荐1500毫米）\n交叉敷设：1000毫米（潮湿地区推荐1500毫米）\n4、配电盘或配电箱：\n平行敷设：300毫米\n交叉敷设：不允许\n##相邻管道之间的净距要求：\n应保证燃气管道和相邻管道的安装、安全维护和修理。\n平行敷设：20毫米 这些净距要求确保了电气设备和燃气管道的安全安装和维护。\n##室内燃气管道与其他管道及设施要求：\n1、与上下水、暖气管道水平净距不应小于100毫米。\n2、与水池边水平净距不应小于200毫米。\n3、与电开关、电插座水平净距不应小于100毫米（但必须保证燃气管道的接口距此处不小于150毫米）。\n4、球阀、管接头严禁安装在电开关和电插座的正下方。\n#输出格式\n按照下列的json格式输出\n{\...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --model /models/OpenGVLab/InternVL3-9B --trust-remote-code from openai import OpenAI client = OpenAI( api_key='EMPTY', base_url=f'http://127.0.0.1:8000/v1', ) model = client.models.list().data[0].id if __name__ == "__ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is hanging bug ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --served-model-name InternVL3-9B --model /models/OpenGVLab/InternVL3-9B --trust-remo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: InternVL3-9B call is hanging bug ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --served-model-name InternVL3-9B --model /models/OpenGVLab/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
