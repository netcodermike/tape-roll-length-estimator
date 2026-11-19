import math

def analyze(payload):
    outer,core,thickness=(payload[key] for key in ['outerDiameterMm','coreDiameterMm','thicknessMm'])
    if any(type(x) not in (int,float) or not math.isfinite(x) or x<=0 for x in [outer,core,thickness]) or outer<core: raise ValueError('Use positive dimensions and outer diameter at least core diameter')
    length=math.pi*(outer**2-core**2)/(4*thickness)/1000
    return {'lengthMeters':round(length,3),'crossSectionMm2':round(math.pi*(outer**2-core**2)/4,3)}

if __name__ == "__main__":
    import json
    from pathlib import Path
    import sys
    try:
        path, = sys.argv[1:]
        result = analyze(json.loads(Path(path).read_text(encoding="utf-8")))
        print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError) as error:
        print(f"Invalid input: {error}", file=sys.stderr)
        sys.exit(2)
