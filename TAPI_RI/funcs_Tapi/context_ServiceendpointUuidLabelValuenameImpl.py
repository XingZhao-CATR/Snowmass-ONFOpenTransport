import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ServiceendpointUuidLabelValuenameImpl:

    @classmethod
    def get(cls, uuid, valueName):
        print 'handling get'
        if uuid in be.Context._serviceEndPoint:
            if valueName in be.Context._serviceEndPoint[uuid].label:
                return be.Context._serviceEndPoint[uuid].label[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')
